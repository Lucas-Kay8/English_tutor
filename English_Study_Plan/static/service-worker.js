// Oli单词冒险 Service Worker
// 用于离线缓存静态资源与API，实现断网可用的PWA体验

const CACHE_NAME = 'oli-vocab-quest-v1';
const ASSETS_TO_CACHE = [
  '/',
  '/static/manifest.json',
  '/static/style.css',
  '/static/script.js',
  '/static/icon.png'
];

// 安装阶段：预缓存核心静态文件
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log('[Service Worker] 正在预缓存关键静态资源...');
      return cache.addAll(ASSETS_TO_CACHE);
    }).then(() => {
      console.log('[Service Worker] 预缓存完成，跳过等待期');
      return self.skipWaiting();
    })
  );
});

// 激活阶段：清理旧版本的冗余缓存
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cache) => {
          if (cache !== CACHE_NAME) {
            console.log('[Service Worker] 正在清除旧缓存:', cache);
            return caches.delete(cache);
          }
        })
      );
    }).then(() => {
      console.log('[Service Worker] 已经接管所有页面控制权');
      return self.clients.claim();
    })
  );
});

// 请求拦截阶段：网络优先，缓存回退
self.addEventListener('fetch', (event) => {
  const url = new URL(event.request.url);

  // 忽略非 GET 请求（如进度保存的 POST 请求）以及 Chrome Extension 等第三方请求
  if (event.request.method !== 'GET' || !url.protocol.startsWith('http')) {
    return;
  }

  event.respondWith(
    fetch(event.request)
      .then((response) => {
        // 请求成功时，将最新的响应存入缓存中（确保后续离线使用）
        if (response && response.status === 200) {
          const responseClone = response.clone();
          caches.open(CACHE_NAME).then((cache) => {
            cache.put(event.request, responseClone);
          });
        }
        return response;
      })
      .catch((err) => {
        console.log('[Service Worker] 网络请求失败，尝试从缓存读取:', event.request.url);
        // 如果断网或请求失败，回退至缓存
        return caches.match(event.request).then((cachedResponse) => {
          if (cachedResponse) {
            return cachedResponse;
          }
          
          // 如果缓存中也没有，并且是导航请求（即主页面），返回 / 的缓存
          if (event.request.mode === 'navigate') {
            return caches.match('/');
          }
          
          // 否则抛出错误或直接失败
          throw err;
        });
      })
  );
});
