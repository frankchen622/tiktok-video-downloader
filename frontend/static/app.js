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
    a.href = href;
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
    
    a.download = filename;
    
    // 点击时通过后端代理下载
    a.addEventListener('click', async (e) => {
      e.preventDefault();
      
      try {
        // 方法1：通过后端 API 代理下载（避免跨域）
        const response = await fetch('/api/proxy-download', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ url: href, filename: filename })
        });
        
        if (response.ok) {
          const blob = await response.blob();
          const downloadUrl = window.URL.createObjectURL(blob);
          const tempLink = document.createElement('a');
          tempLink.href = downloadUrl;
          tempLink.download = filename;
          document.body.appendChild(tempLink);
          tempLink.click();
          document.body.removeChild(tempLink);
          window.URL.revokeObjectURL(downloadUrl);
        } else {
          // 回退方案：直接使用原始链接
          throw new Error('Proxy failed');
        }
      } catch (err) {
        // 方法2：如果后端不可用，使用 iframe 隐藏下载
        const iframe = document.createElement('iframe');
        iframe.style.display = 'none';
        iframe.src = href;
        document.body.appendChild(iframe);
        
        // 5秒后移除 iframe
        setTimeout(() => {
          document.body.removeChild(iframe);
        }, 5000);
      }
    });
    
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

    // Buttons — matches reference image layout
    resultActions.innerHTML = '';

    if (data.video_url) {
      resultActions.appendChild(
        makeDlBtn('Download Without Watermark', data.video_url, true)
      );
    }

    // Watermark version from formats fallback (second format if exists)
    if (data.formats && data.formats.length > 1) {
      const wm = data.formats[1];
      resultActions.appendChild(
        makeDlBtn('Download with Watermark', wm.url, false)
      );
    } else if (data.video_url) {
      // Show as alternate quality link
      resultActions.appendChild(
        makeDlBtn('Download MP4', data.video_url, false)
      );
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
