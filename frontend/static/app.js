(() => {
  'use strict';

  const form       = document.getElementById('downloaderForm');
  const input      = document.getElementById('videoUrl');
  const submitBtn  = document.getElementById('submitBtn');
  const btnText    = submitBtn.querySelector('.btn-text');
  const btnSpinner = submitBtn.querySelector('.btn-spinner');
  const urlError   = document.getElementById('urlError');

  const resultCard    = document.getElementById('resultCard');
  const resultThumb   = document.getElementById('resultThumb');
  const resultTitle   = document.getElementById('resultTitle');
  const resultAuthor  = document.getElementById('resultAuthor');
  const resultActions = document.getElementById('resultActions');

  const errorCard    = document.getElementById('errorCard');

  // ── Initialize button state ────────────────────────────────────────────────
  
  // Ensure button is in normal state on page load
  submitBtn.disabled = false;
  btnText.hidden = false;
  btnSpinner.hidden = true;

  // ── Helpers ────────────────────────────────────────────────────────────────

  function setLoading(on) {
    submitBtn.disabled = on;
    btnText.hidden     = on;
    btnSpinner.hidden  = !on;
  }

  function hideResults() {
    resultCard.hidden = true;
    errorCard.hidden  = true;
    errorCard.textContent = '';
    urlError.textContent = '';
  }

  function showError(msg) {
    errorCard.textContent = msg;
    errorCard.hidden  = false;
    resultCard.hidden = true;
  }

  function formatSize(bytes) {
    if (!bytes) return '';
    if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(0)} KB`;
    return `${(bytes / (1024 * 1024)).toFixed(1)} MB`;
  }

  function makeDlBtn(label, href, primary = false) {
    const a = document.createElement('a');
    a.className = primary ? 'dl-btn dl-btn-primary' : 'dl-btn dl-btn-secondary';
    a.textContent = label;
    
    // 生成文件名
    const timestamp = Date.now();
    let filename = 'tiktok_video_' + timestamp;
    
    if (label.includes('Watermark')) {
      filename = label.includes('Without') ? 'tiktok_no_watermark_' + timestamp + '.mp4' : 'tiktok_with_watermark_' + timestamp + '.mp4';
    } else if (label.includes('Thumbnail')) {
      filename = 'tiktok_thumbnail_' + timestamp + '.jpg';
    } else if (label.includes('MP4')) {
      filename = 'tiktok_video_' + timestamp + '.mp4';
    } else {
      filename = 'tiktok_download_' + timestamp + '.mp4';
    }
    
    // 直接链接到视频 URL（让浏览器尝试下载）
    // 不经过代理，因为 TikTok 的防盗链可能阻止服务器端代理
    a.href = href;
    a.download = filename;
    
    return a;
  }

  // ── Form submit ────────────────────────────────────────────────────────────

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    hideResults();

    const url = input.value.trim();
    if (!url) {
      urlError.textContent = 'Please paste a TikTok video link.';
      input.focus();
      return;
    }
    if (!url.startsWith('http')) {
      urlError.textContent = 'Looks like an invalid link. Make sure to copy the full URL.';
      input.focus();
      return;
    }

    setLoading(true);

    try {
      const res = await fetch('/api/parse', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url }),
      });

      const data = await res.json();

      if (!res.ok) {
        showError(data.detail || 'Could not parse this link. Please check it and try again.');
        return;
      }

      renderResult(data);

    } catch (err) {
      showError('Network error. Please check your connection and try again.');
    } finally {
      setLoading(false);
    }
  });

  // ── Render result ──────────────────────────────────────────────────────────

  function renderResult(data) {
    // Thumbnail
    if (data.thumbnail) {
      resultThumb.src = data.thumbnail;
      resultThumb.alt = data.title || 'Video thumbnail';
    } else {
      resultThumb.src = '';
      resultThumb.alt = '';
    }

    // Meta
    resultAuthor.textContent = data.author ? `User: @${data.author}` : '';
    resultTitle.textContent  = data.title  || 'TikTok Video';

    // Buttons — use original TikTok URL for real server-side download
    resultActions.innerHTML = '';

    // Get the original TikTok URL from the input
    const originalUrl = input.value.trim();

    if (originalUrl) {
      // Primary download button - uses yt-dlp server-side download
      const downloadBtn = document.createElement('a');
      downloadBtn.className = 'dl-btn dl-btn-primary';
      downloadBtn.textContent = 'Download Video';
      downloadBtn.href = `/api/download?url=${encodeURIComponent(originalUrl)}`;
      downloadBtn.target = '_blank'; // Open in new tab to show download progress
      resultActions.appendChild(downloadBtn);
    }

    // Thumbnail
    if (data.thumbnail) {
      resultActions.appendChild(
        makeDlBtn('🖼 Save Thumbnail', data.thumbnail, false)
      );
    }

    resultCard.hidden = false;
    resultCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }

  // ── Auto-submit on paste ───────────────────────────────────────────────────
  input.addEventListener('paste', () => {
    setTimeout(() => {
      if (input.value.trim().startsWith('http')) {
        form.dispatchEvent(new Event('submit', { cancelable: true }));
      }
    }, 80);
  });

})();
