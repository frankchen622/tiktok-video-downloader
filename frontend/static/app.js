(() => {
  'use strict';

  const form      = document.getElementById('downloaderForm');
  const input     = document.getElementById('videoUrl');
  const submitBtn = document.getElementById('submitBtn');
  const btnText   = submitBtn.querySelector('.btn-text');
  const btnSpinner= submitBtn.querySelector('.btn-spinner');
  const urlError  = document.getElementById('urlError');

  const resultSection = document.getElementById('resultSection');
  const resultThumb   = document.getElementById('resultThumb');
  const resultTitle   = document.getElementById('resultTitle');
  const resultAuthor  = document.getElementById('resultAuthor');
  const resultActions = document.getElementById('resultActions');

  const errorSection  = document.getElementById('errorSection');
  const errorMessage  = document.getElementById('errorMessage');

  // ── Helpers ────────────────────────────────────────────────────────────────

  function setLoading(on) {
    submitBtn.disabled = on;
    btnText.hidden     = on;
    btnSpinner.hidden  = !on;
  }

  function hideAll() {
    resultSection.hidden = true;
    errorSection.hidden  = true;
    urlError.textContent = '';
  }

  function showError(msg) {
    errorMessage.textContent = msg;
    errorSection.hidden = false;
    resultSection.hidden = true;
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
    a.target = '_blank';
    a.rel = 'noopener noreferrer';
    // Use download attribute as a hint — works when same-origin; cross-origin falls back to tab
    a.download = '';
    a.textContent = label;
    return a;
  }

  // ── Form submit ────────────────────────────────────────────────────────────

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    hideAll();

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
    resultTitle.textContent  = data.title  || 'TikTok Video';
    resultAuthor.textContent = data.author ? `@${data.author}` : '';

    // Action buttons
    resultActions.innerHTML = '';

    if (data.video_url) {
      resultActions.appendChild(
        makeDlBtn('⬇ Download Video (Best)', data.video_url, true)
      );
    }

    // Additional formats
    if (data.formats && data.formats.length > 1) {
      data.formats.slice(0, 5).forEach((f) => {
        const size  = formatSize(f.filesize);
        const label = `${f.label}${size ? ` · ${size}` : ''} .${f.ext}`;
        resultActions.appendChild(makeDlBtn(label, f.url));
      });
    }

    // Thumbnail download
    if (data.thumbnail) {
      resultActions.appendChild(makeDlBtn('🖼 Download Thumbnail', data.thumbnail));
    }

    resultSection.hidden = false;
    resultSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }

  // ── Paste shortcut ─────────────────────────────────────────────────────────
  // Auto-submit when user pastes directly into the input
  input.addEventListener('paste', () => {
    setTimeout(() => {
      if (input.value.trim().startsWith('http')) {
        form.dispatchEvent(new Event('submit', { cancelable: true }));
      }
    }, 80);
  });

})();
