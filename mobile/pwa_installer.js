/**
 * CORTEX PWA INSTALLER & SERVICE WORKER CONTROLLER
 * Full Chrome PWA Install Prompt, Native App Hooks, and Offline Sync
 * Features: Automatic removal after first touch/click by user + persistent state
 */

(function () {
  'use strict';

  let deferredInstallPrompt = null;

  function hasUserDismissedInstall() {
    try {
      return localStorage.getItem('cortex_install_dismissed') === 'true' ||
             window.matchMedia('(display-mode: standalone)').matches ||
             window.navigator.standalone === true;
    } catch (e) {
      return false;
    }
  }

  function removeInstallButtons() {
    const buttons = document.querySelectorAll('.btn-pwa-install, #btn-pwa-install, #hud-install-btn, #nav-install-btn, [data-action="install-pwa"]');
    buttons.forEach((btn) => {
      btn.style.transition = 'opacity 0.25s ease, transform 0.25s ease';
      btn.style.opacity = '0';
      btn.style.transform = 'scale(0.8)';
      setTimeout(() => {
        if (btn && btn.parentNode) {
          btn.remove();
        }
      }, 260);
    });
  }

  // 1. Register Service Worker with appropriate relative path
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
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
    e.preventDefault();
    deferredInstallPrompt = e;
    console.log('[PWA] Captured beforeinstallprompt event. Ready for Chrome installation.');

    // Only unhide install buttons if user has NOT already touched/dismissed it
    if (!hasUserDismissedInstall()) {
      updateInstallButtons(true);
    } else {
      removeInstallButtons();
    }
  });

  // 3. User trigger install method (Immediately removes button on first touch)
  window.triggerPwaInstall = async function () {
    // Instantly mark as touched and remove button from UI
    try {
      localStorage.setItem('cortex_install_dismissed', 'true');
    } catch (e) {}
    removeInstallButtons();

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
    } else {
      // Friendly fallback guidance if already installed or triggered on unsupported environment
      showInstallInstructions();
    }
  };

  // 4. Handle successful installation
  window.addEventListener('appinstalled', (evt) => {
    console.log('[PWA] Cortex Quest app was installed successfully on Chrome!', evt);
    try {
      localStorage.setItem('cortex_install_dismissed', 'true');
    } catch (e) {}
    deferredInstallPrompt = null;
    removeInstallButtons();

    // Celebration feedback
    if (window.DuoSound && typeof DuoSound.playFanfare === 'function') {
      DuoSound.playFanfare();
    }
    showToastNotification('🎉 Cortex App installed! You can now launch it directly from your home screen or desktop.');
  });

  // Helper to toggle install buttons visibility
  function updateInstallButtons(visible) {
    if (hasUserDismissedInstall()) {
      removeInstallButtons();
      return;
    }
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

  // Hook first touch and dismissal on DOM ready
  document.addEventListener('DOMContentLoaded', () => {
    if (hasUserDismissedInstall()) {
      removeInstallButtons();
      return;
    }

    const buttons = document.querySelectorAll('.btn-pwa-install, #btn-pwa-install, #hud-install-btn, #nav-install-btn, [data-action="install-pwa"]');
    buttons.forEach((btn) => {
      // On first touch or click by user, remove immediately
      const handleFirstTouch = () => {
        try {
          localStorage.setItem('cortex_install_dismissed', 'true');
        } catch (e) {}
        removeInstallButtons();
      };

      btn.addEventListener('touchstart', handleFirstTouch, { passive: true, once: true });
      btn.addEventListener('mousedown', handleFirstTouch, { once: true });
    });
  });
})();
