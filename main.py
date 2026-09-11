import os
import asyncio
import logging
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
import yt_dlp

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

limiter = Limiter(key_func=get_remote_address)
app = FastAPI(title="TikTok Downloader API")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://dltk.io",
        "https://www.dltk.io",
        "http://localhost:3000",
        "http://localhost:8000",
    ],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
    allow_credentials=True,
)

# Serve frontend static files
frontend_path = os.path.join(os.path.dirname(__file__), "frontend")
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


@app.get("/health")
async def health_check():
    """Lightweight health check for Railway"""
    return {"status": "ok", "version": "1.0.0"}


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


# ========== 中文站路由 (Chinese Localized URLs) ==========

@app.get("/zh")
async def serve_index_zh():
    """中文首页 - TikTok视频下载"""
    return FileResponse(os.path.join(frontend_path, "zh", "index.html"))


@app.get("/zh/yinpin")
async def serve_mp3_zh():
    """中文MP3转换页面"""
    return FileResponse(os.path.join(frontend_path, "zh", "yinpin.html"))


@app.get("/zh/fengmian")
async def serve_thumbnail_zh():
    """中文封面图下载页面"""
    return FileResponse(os.path.join(frontend_path, "zh", "fengmian.html"))


@app.get("/zh/kuaipai")
async def serve_story_zh():
    """中文快拍下载页面"""
    return FileResponse(os.path.join(frontend_path, "zh", "kuaipai.html"))


# 中文法律页面路由
@app.get("/zh/{page_name}")
async def serve_page_zh(page_name: str):
    """中文法律/信息页面"""
    allowed_pages = ["lianxi", "yinsi", "tiaokuan", "mianze", "banquan", "cookie"]
    if page_name not in allowed_pages:
        raise HTTPException(status_code=404, detail="页面不存在")
    
    # 映射到对应的HTML文件
    page_map = {
        "lianxi": "lianxi.html",      # 联系我们
        "yinsi": "yinsi.html",          # 隐私政策
        "tiaokuan": "tiaokuan.html",    # 使用条款
        "mianze": "mianze.html",        # 免责声明
        "banquan": "banquan.html",      # 版权政策
        "cookie": "cookie.html"          # Cookie政策
    }
    
    filename = page_map.get(page_name)
    if not filename:
        raise HTTPException(status_code=404, detail="页面不存在")
    
    return FileResponse(os.path.join(frontend_path, "zh", "pages", filename))


@app.post("/api/parse")
@limiter.limit("20/minute")
async def parse_video(request: Request, body: ParseRequest):
    client_ip = get_remote_address(request)
    logger.info(f"Parse request from {client_ip}: {body.url[:50]}...")
    
    try:
        url = sanitize_url(body.url)
    except ValueError:
        logger.warning(f"Invalid URL from {client_ip}: {body.url}")
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


# Real download endpoint using yt-dlp
import tempfile
import uuid
from pathlib import Path

@app.get("/api/download")
@limiter.limit("10/minute")
async def download_video(request: Request, url: str, format: str = "video"):
    """Download video or audio using yt-dlp and serve it"""
    client_ip = get_remote_address(request)
    logger.info(f"Download request ({format}) from {client_ip}: {url[:50]}...")
    
    try:
        url = sanitize_url(url)
    except ValueError:
        logger.warning(f"Invalid download URL from {client_ip}: {url}")
        raise HTTPException(status_code=400, detail="Invalid URL format")
    
    # Create temp directory for downloads
    temp_dir = Path(tempfile.gettempdir()) / "tiktok_downloads"
    temp_dir.mkdir(exist_ok=True)
    
    # Generate unique filename
    video_id = str(uuid.uuid4())[:8]
    output_template = str(temp_dir / f"{video_id}.%(ext)s")
    
    # Configure yt-dlp options based on format
    if format == "mp3":
        ydl_opts = {
            "quiet": True,
            "no_warnings": True,
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "320",
            }],
            "http_headers": {
                "User-Agent": (
                    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) "
                    "AppleWebKit/605.1.15 (KHTML, like Gecko) "
                    "Version/17.0 Mobile/15E148 Safari/604.1"
                ),
                "Referer": "https://www.tiktok.com/",
            },
            "retries": 3,
            "socket_timeout": 30,
        }
    else:
        ydl_opts = {
            "quiet": True,
            "no_warnings": True,
            "format": "download_addr-0/best[ext=mp4]/best",
            "outtmpl": output_template,
            "http_headers": {
                "User-Agent": (
                    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) "
                    "AppleWebKit/605.1.15 (KHTML, like Gecko) "
                    "Version/17.0 Mobile/15E148 Safari/604.1"
                ),
                "Referer": "https://www.tiktok.com/",
            },
            "retries": 3,
            "socket_timeout": 30,
        }
    
    loop = asyncio.get_event_loop()
    
    def _download():
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            # Find the downloaded file
            if format == "mp3":
                ext = "mp3"
            else:
                ext = info.get("ext", "mp4")
            downloaded_file = temp_dir / f"{video_id}.{ext}"
            return downloaded_file, info.get("title", "tiktok")
    
    try:
        downloaded_file, title = await loop.run_in_executor(None, _download)
        
        if not downloaded_file.exists():
            raise HTTPException(status_code=500, detail="Download failed")
        
        # Clean filename
        safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_'))[:50]
        if format == "mp3":
            filename = f"{safe_title}.mp3" if safe_title else "tiktok_audio.mp3"
            media_type = "audio/mpeg"
        else:
            filename = f"{safe_title}.mp4" if safe_title else "tiktok_video.mp4"
            media_type = "video/mp4"
        
        # Return file and schedule cleanup
        def cleanup():
            try:
                if downloaded_file.exists():
                    downloaded_file.unlink()
            except:
                pass
        
        response = FileResponse(
            path=str(downloaded_file),
            media_type=media_type,
            filename=filename,
            background=cleanup
        )
        return response
        
    except yt_dlp.utils.DownloadError as e:
        raise HTTPException(status_code=400, detail=f"Download failed: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")


# Thumbnail download endpoint
import httpx

@app.get("/api/download-thumbnail")
@limiter.limit("20/minute")
async def download_thumbnail(request: Request, url: str):
    """Download thumbnail image and serve it with proper headers for download"""
    try:
        url = sanitize_url(url)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid URL format")
    
    # Create temp directory
    temp_dir = Path(tempfile.gettempdir()) / "tiktok_downloads"
    temp_dir.mkdir(exist_ok=True)
    
    # Generate unique filename
    thumb_id = str(uuid.uuid4())[:8]
    temp_file = temp_dir / f"thumb_{thumb_id}.jpg"
    
    try:
        # Download the image
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get(url, follow_redirects=True)
            response.raise_for_status()
            
            # Write to temp file
            with open(temp_file, 'wb') as f:
                f.write(response.content)
        
        # Return file and schedule cleanup
        def cleanup():
            try:
                if temp_file.exists():
                    temp_file.unlink()
            except:
                pass
        
        return FileResponse(
            path=str(temp_file),
            media_type="image/jpeg",
            filename=f"tiktok_thumbnail_{thumb_id}.jpg",
            background=cleanup
        )
        
    except httpx.HTTPError as e:
        raise HTTPException(status_code=400, detail=f"Failed to download thumbnail: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")


