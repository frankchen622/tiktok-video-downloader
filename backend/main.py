import os
import asyncio
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
import yt_dlp

limiter = Limiter(key_func=get_remote_address)
app = FastAPI(title="TikTok Downloader API")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# Serve frontend static files
frontend_path = os.path.join(os.path.dirname(__file__), "..", "frontend")
app.mount("/static", StaticFiles(directory=os.path.join(frontend_path, "static")), name="static")


class ParseRequest(BaseModel):
    url: str


def sanitize_url(url: str) -> str:
    url = url.strip()
    if not url.startswith("http"):
        raise ValueError("Invalid URL")
    return url


@app.get("/")
async def serve_index():
    return FileResponse(os.path.join(frontend_path, "index.html"))


@app.get("/robots.txt")
async def serve_robots():
    return FileResponse(os.path.join(frontend_path, "robots.txt"), media_type="text/plain")


@app.get("/sitemap.xml")
async def serve_sitemap():
    return FileResponse(os.path.join(frontend_path, "sitemap.xml"), media_type="application/xml")


@app.get("/manifest.json")
async def serve_manifest():
    return FileResponse(os.path.join(frontend_path, "manifest.json"), media_type="application/json")


@app.get("/mp3.html")
async def serve_mp3():
    return FileResponse(os.path.join(frontend_path, "mp3.html"))


@app.get("/thumbnail.html")
async def serve_thumbnail():
    return FileResponse(os.path.join(frontend_path, "thumbnail.html"))


@app.get("/story.html")
async def serve_story():
    return FileResponse(os.path.join(frontend_path, "story.html"))


@app.get("/pages/{page_name}")
async def serve_page(page_name: str):
    # Serve legal/info pages
    allowed_pages = ["contact.html", "privacy.html", "terms.html", "disclaimer.html", "dmca.html", "cookies.html"]
    if page_name not in allowed_pages:
        raise HTTPException(status_code=404, detail="Page not found")
    return FileResponse(os.path.join(frontend_path, "pages", page_name))


@app.post("/api/parse")
@limiter.limit("20/minute")
async def parse_video(request: Request, body: ParseRequest):
    try:
        url = sanitize_url(body.url)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid URL format")

    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "extract_flat": False,
        # Try no-watermark format first, fall back to best available
        "format": "download_addr-0/bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio/best[ext=mp4]/best",
        # Mimic a real browser to avoid bot detection
        "http_headers": {
            "User-Agent": (
                "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) "
                "AppleWebKit/605.1.15 (KHTML, like Gecko) "
                "Version/17.0 Mobile/15E148 Safari/604.1"
            ),
            "Referer": "https://www.tiktok.com/",
            "Accept-Language": "en-US,en;q=0.9",
        },
        # Retry on transient failures
        "retries": 3,
        "socket_timeout": 30,
        # Suppress the "merge output format" warning
        "merge_output_format": "mp4",
    }

    loop = asyncio.get_event_loop()

    def _extract():
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            return ydl.extract_info(url, download=False)

    try:
        info = await loop.run_in_executor(None, _extract)
    except yt_dlp.utils.DownloadError as e:
        err = str(e)
        # Surface a cleaner message for common cases
        if "Unable to download" in err or "HTTP Error" in err:
            raise HTTPException(
                status_code=400,
                detail="TikTok blocked this request. Try again in a moment or use a different link.",
            )
        raise HTTPException(status_code=400, detail=f"Could not parse video: {err}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

    # Collect available formats — prefer higher resolution, skip audio-only
    formats = []
    seen_urls = set()
    for f in info.get("formats") or []:
        furl = f.get("url")
        if not furl or furl in seen_urls:
            continue
        # Skip audio-only streams in the list (keep them only as MP3 option)
        if f.get("vcodec") == "none" and f.get("acodec") != "none":
            continue
        seen_urls.add(furl)
        height = f.get("height") or 0
        label = f.get("format_note") or (f"{height}p" if height else f.get("format_id", "video"))
        formats.append({
            "label": label,
            "url": furl,
            "ext": f.get("ext", "mp4"),
            "filesize": f.get("filesize"),
            "height": height,
        })

    # Sort by resolution descending
    formats.sort(key=lambda x: x.get("height") or 0, reverse=True)

    # Best single URL: prefer the top-quality format URL, fall back to info["url"]
    best_url = (formats[0]["url"] if formats else None) or info.get("url")

    # Thumbnail: prefer a high-res one if multiple are available
    thumbnails = info.get("thumbnails") or []
    thumbnail = info.get("thumbnail", "")
    if thumbnails:
        best_thumb = max(
            (t for t in thumbnails if t.get("url")),
            key=lambda t: (t.get("width") or 0) * (t.get("height") or 0),
            default=None,
        )
        if best_thumb:
            thumbnail = best_thumb["url"]

    return {
        "title": info.get("title", ""),
        "author": info.get("uploader", "") or info.get("creator", ""),
        "thumbnail": thumbnail,
        "duration": info.get("duration"),
        "video_url": best_url,
        "formats": formats[:6],
    }


# Proxy download endpoint to avoid CORS issues
from fastapi.responses import StreamingResponse
import httpx

class ProxyDownloadRequest(BaseModel):
    url: str
    filename: str

@app.post("/api/proxy-download")
@limiter.limit("50/minute")
async def proxy_download(request: Request, body: ProxyDownloadRequest):
    """Proxy download to avoid CORS and force download"""
    try:
        url = body.url
        filename = body.filename
        
        # Stream the file from TikTok servers
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.get(url, follow_redirects=True)
            
            if response.status_code != 200:
                raise HTTPException(status_code=400, detail="Could not download file")
            
            # Determine content type
            content_type = response.headers.get('content-type', 'application/octet-stream')
            
            # Return as streaming response with download headers
            return StreamingResponse(
                iter([response.content]),
                media_type=content_type,
                headers={
                    'Content-Disposition': f'attachment; filename="{filename}"',
                    'Content-Length': str(len(response.content))
                }
            )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Download failed: {str(e)}")
