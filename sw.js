/**
 * CORTEX PWA SERVICE WORKER
 * Offline Caching, Stale-While-Revalidate & Chrome Installability
 */

const CACHE_NAME = 'cortex-pwa-v1.2';

const PRECACHE_ASSETS = [
  './',
  './index.html',
  './mobile/index.html',
  './msme_duo.html',
  './public_exam_duo.html',
  './roadmap_notes.html',
  './subjects.html',
  './cava.html',
  './topic_study.html',
  './style.css',
  './mobile/game.css',
  './app.js',
  './theme_sync.js',
  './lecture_data.js',
  './msme_data.js',
  './public_exam_data.js',
  './duolingo_engine.js',
  './roadmap_data.js',
  './roadmap_engine.js',
  './mobile/mobile_data.js',
  './mobile/game.js',
  './manifest.json',
  './mobile/manifest.json',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './icons/icon-maskable-512.png',
  './icons/apple-touch-icon.png',
  './icons/favicon.png',
  './mobile/assets/flowcharts/flowchart_msme_classification.svg',
  './mobile/assets/flowcharts/flowchart_delayed_payments.svg',
  './mobile/assets/flowcharts/flowchart_pm_vishwakarma.svg',
  './mobile/assets/flowcharts/flowchart_dwarfism_vs_mittelstand.svg',
  './Filtered_Questions/MSME_best_questions.json'
];

// Install: Cache Shell & Precache Assets
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      // Use addAll with error handling for optional assets
      return Promise.allSettled(
        PRECACHE_ASSETS.map((url) =>
          cache.add(url).catch((err) => {
            console.warn(`[SW] Precache item failed: ${url}`, err);
          })
        )
      );
    }).then(() => self.skipWaiting())
  );
});

// Activate: Clean Up Old Caches
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((key) => {
          if (key !== CACHE_NAME) {
            console.log('[SW] Deleting old cache:', key);
            return caches.delete(key);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

// Fetch: Stale-While-Revalidate Strategy with Network Fallback
self.addEventListener('fetch', (event) => {
  // Only handle GET requests and http/https schemes
  if (event.request.method !== 'GET') return;
  const url = new URL(event.request.url);
  if (!url.protocol.startsWith('http')) return;

  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      const fetchPromise = fetch(event.request)
        .then((networkResponse) => {
          if (networkResponse && networkResponse.status === 200) {
            const responseClone = networkResponse.clone();
            caches.open(CACHE_NAME).then((cache) => {
              cache.put(event.request, responseClone);
            });
          }
          return networkResponse;
        })
        .catch(() => {
          // If offline and request is for a web page, return cached index
          if (event.request.mode === 'navigate') {
            return caches.match('./mobile/index.html') || caches.match('./index.html');
          }
          return null;
        });

      return cachedResponse || fetchPromise;
    })
  );
});
