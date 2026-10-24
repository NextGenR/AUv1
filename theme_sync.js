/**
 * SAMSUNG ONE UI GLOBAL THEME SYNC
 * Pure AMOLED Dark Mode (#000000) & Soft Ceramic Porcelain Light Mode (#f2f4f8)
 * Synchronizes across desktop web pages and mobile game suite
 */

(function () {
  'use strict';

  function getSavedTheme() {
    return localStorage.getItem('samsung_ui_theme') || 'samsung-dark';
  }

  function applyTheme(theme) {
    const isLight = theme === 'samsung-light';
    localStorage.setItem('samsung_ui_theme', theme);
    localStorage.setItem('cortex_roadmap_dark', isLight ? 'false' : 'true');

    if (isLight) {
      document.body.classList.remove('samsung-dark', 'dark-theme');
      document.body.classList.add('samsung-light', 'light-theme');
    } else {
      document.body.classList.remove('samsung-light', 'light-theme');
      document.body.classList.add('samsung-dark', 'dark-theme');
    }

    // Update Theme Toggle Buttons
    const buttons = document.querySelectorAll('#global-theme-toggle, #btn-theme-toggle, #samsung-theme-toggle');
    buttons.forEach(btn => {
      const icon = btn.querySelector('#global-theme-icon, #theme-btn-icon, #theme-toggle-icon');
      const text = btn.querySelector('#global-theme-text, #theme-btn-text, #theme-toggle-text');
      if (icon) icon.textContent = isLight ? '☀️' : '🌙';
      if (text) text.textContent = isLight ? 'Light UI' : 'Dark UI';
    });

    // Update Theme-Color Meta Tag
    const metaTheme = document.querySelector('meta[name="theme-color"]');
    if (metaTheme) {
      metaTheme.setAttribute('content', isLight ? '#f2f4f8' : '#000000');
    }

    // Dispatch global event for subscribers (like SVG redrawing)
    window.dispatchEvent(new CustomEvent('samsungThemeChanged', { detail: { theme, isLight } }));
  }

  function toggleTheme() {
    const current = getSavedTheme();
    const next = current === 'samsung-dark' ? 'samsung-light' : 'samsung-dark';
    applyTheme(next);
  }

  function init() {
    // Apply initial theme immediately
    applyTheme(getSavedTheme());

    // Bind event listeners to any theme toggle buttons on the page
    const buttons = document.querySelectorAll('#global-theme-toggle, #btn-theme-toggle');
    buttons.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        toggleTheme();
      });
    });
  }

  // Run as early as possible to prevent flash of wrong theme
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  window.SamsungTheme = {
    get: getSavedTheme,
    set: applyTheme,
    toggle: toggleTheme
  };

})();
