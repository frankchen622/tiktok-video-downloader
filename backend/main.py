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
        # Request a non-watermarked format when available
        "format": "download_addr-0/bestvideo+bestaudio/best",
    }

    loop = asyncio.get_event_loop()

    def _extract():
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            return ydl.extract_info(url, download=False)

    try:
        info = await loop.run_in_executor(None, _extract)
    except yt_dlp.utils.DownloadError as e:
        raise HTTPException(status_code=400, detail=f"Could not parse video: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Unexpected error while parsing video")

    # Collect available formats
    formats = []
    seen = set()
    for f in info.get("formats") or []:
        if not f.get("url"):
            continue
        label = f.get("format_note") or f.get("height") or f.get("format_id", "")
        label = str(label)
        if label in seen:
            continue
        seen.add(label)
        formats.append({
            "label": label,
            "url": f["url"],
            "ext": f.get("ext", "mp4"),
            "filesize": f.get("filesize"),
        })

    # Best single URL fallback
    best_url = info.get("url") or (formats[0]["url"] if formats else None)

    return {
        "title": info.get("title", ""),
        "author": info.get("uploader", ""),
        "thumbnail": info.get("thumbnail", ""),
        "duration": info.get("duration"),
        "video_url": best_url,
        "formats": formats[:8],  # Cap to avoid huge payloads
    }
