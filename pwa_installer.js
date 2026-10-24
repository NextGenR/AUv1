/**
 * CORTEX PWA INSTALLER & SERVICE WORKER CONTROLLER
 * Full Chrome PWA Install Prompt, Native App Hooks, and Offline Sync
 */

(function () {
  'use strict';

  let deferredInstallPrompt = null;

  // 1. Register Service Worker with appropriate relative path
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
      // Determine if we are in /mobile/ or root directory
      const isMobileSubdir = window.location.pathname.includes('/mobile/');
      const swUrl = isMobileSubdir ? 'sw.js' : 'sw.js';

      navigator.serviceWorker.register(swUrl)
        .then((registration) => {
          console.log('[PWA] Service Worker registered successfully! Scope:', registration.scope);
        })
        .catch((error) => {
          console.warn('[PWA] Service Worker registration failed:', error);
        });
    });
  }

  // 2. Capture Chrome 'beforeinstallprompt' event
  window.addEventListener('beforeinstallprompt', (e) => {
    // Prevent default mini-infobar on Android
    e.preventDefault();
    deferredInstallPrompt = e;
    console.log('[PWA] Captured beforeinstallprompt event. Ready for Chrome installation.');

    // Unhide install buttons in the UI
    updateInstallButtons(true);
  });

  // 3. User trigger install method
  window.triggerPwaInstall = async function () {
    if (deferredInstallPrompt) {
      // Show native Chrome install prompt dialog
      deferredInstallPrompt.prompt();
      const choiceResult = await deferredInstallPrompt.userChoice;
      console.log('[PWA] User install choice:', choiceResult.outcome);

      if (choiceResult.outcome === 'accepted') {
        console.log('[PWA] User accepted the Chrome install prompt');
      } else {
        console.log('[PWA] User dismissed the Chrome install prompt');
      }
      deferredInstallPrompt = null;
      updateInstallButtons(false);
    } else {
      // Friendly fallback guidance if already installed or triggered on unsupported environment
      showInstallInstructions();
    }
  };

  // 4. Handle successful installation
  window.addEventListener('appinstalled', (evt) => {
    console.log('[PWA] Cortex Quest app was installed successfully on Chrome!', evt);
    deferredInstallPrompt = null;
    updateInstallButtons(false);

    // Optional celebration toast
    if (window.DuoSound && typeof DuoSound.playFanfare === 'function') {
      DuoSound.playFanfare();
    }
    showToastNotification('🎉 Cortex App installed! You can now launch it directly from your home screen or desktop.');
  });

  // Helper to toggle install buttons visibility
  function updateInstallButtons(visible) {
    const buttons = document.querySelectorAll('.btn-pwa-install, #btn-pwa-install, #hud-install-btn, #nav-install-btn');
    buttons.forEach((btn) => {
      btn.style.display = visible ? 'inline-flex' : 'none';
    });
  }

  function showInstallInstructions() {
    const isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream;
    if (isIOS) {
      alert("📲 To Install on iPhone / iPad:\n1. Tap the Share button (square with arrow ↑) in Safari.\n2. Scroll down and tap 'Add to Home Screen'.");
    } else {
      alert("✨ How to install on Google Chrome:\n1. Click the 'Install App' icon (🖥️ / ⬇️) in Chrome's address bar (right side).\n   OR\n2. Click the three dots (⋮) in the top-right corner of Chrome -> Select 'Install Cortex Quest...'");
    }
  }

  function showToastNotification(msg) {
    const toast = document.createElement('div');
    toast.style.cssText = `
      position: fixed;
      bottom: 24px;
      left: 50%;
      transform: translateX(-50%);
      background: #2563eb;
      color: #fff;
      padding: 12px 20px;
      border-radius: 999px;
      font-family: 'Outfit', sans-serif;
      font-size: 0.88rem;
      font-weight: 800;
      box-shadow: 0 10px 25px rgba(37, 99, 235, 0.5);
      z-index: 9999;
      display: flex;
      align-items: center;
      gap: 8px;
      animation: fadeInToast 0.3s ease;
    `;
    toast.textContent = msg;
    document.body.appendChild(toast);
    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transition = 'opacity 0.4s ease';
      setTimeout(() => toast.remove(), 400);
    }, 4000);
  }

  // Hook any elements with data-action="install-pwa"
  document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('[data-action="install-pwa"]').forEach((el) => {
      el.addEventListener('click', (e) => {
        e.preventDefault();
        window.triggerPwaInstall();
      });
    });
  });
})();
