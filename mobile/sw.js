/**
 * CORTEX MOBILE PWA SERVICE WORKER
 */

const CACHE_NAME = 'cortex-mobile-v1.2';

const ASSETS = [
  './',
  './index.html',
  './game.css',
  './game.js',
  './mobile_data.js',
  './manifest.json',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './icons/icon-maskable-512.png',
  './icons/apple-touch-icon.png',
  './icons/favicon.png',
  './assets/flowcharts/flowchart_msme_classification.svg',
  './assets/flowcharts/flowchart_delayed_payments.svg',
  './assets/flowcharts/flowchart_pm_vishwakarma.svg',
  './assets/flowcharts/flowchart_dwarfism_vs_mittelstand.svg',
  '../msme_data.js',
  '../public_exam_data.js',
  '../lecture_data.js'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return Promise.allSettled(
        ASSETS.map((url) =>
          cache.add(url).catch((err) => {
            console.warn(`[Mobile SW] Precache item failed: ${url}`, err);
          })
        )
      );
    }).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((key) => {
          if (key !== CACHE_NAME) {
            return caches.delete(key);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;
  const url = new URL(event.request.url);
  if (!url.protocol.startsWith('http')) return;

  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      const fetchPromise = fetch(event.request)
        .then((networkResponse) => {
          if (networkResponse && networkResponse.status === 200) {
            const clone = networkResponse.clone();
            caches.open(CACHE_NAME).then((cache) => {
              cache.put(event.request, clone);
            });
          }
          return networkResponse;
        })
        .catch(() => {
          if (event.request.mode === 'navigate') {
            return caches.match('./index.html');
          }
          return null;
        });

      return cachedResponse || fetchPromise;
    })
  );
});
