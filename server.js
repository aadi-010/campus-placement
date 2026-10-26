/**
 * Zero-dependency Node.js Development & Proxy Server
 * Serves static assets and provides a transparent streaming proxy for Ollama & Gemini API.
 */
const http = require('http');
const https = require('https');
const fs = require('fs');
const path = require('path');
const url = require('url');

const PORT = process.env.PORT || 3000;
const OLLAMA_HOST = process.env.OLLAMA_HOST || '127.0.0.1';
const OLLAMA_PORT = process.env.OLLAMA_PORT || 11434;

const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.md': 'text/markdown; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.gif': 'image/gif',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon'
};

const server = http.createServer((req, res) => {
  // Add permissive CORS headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization, x-goog-api-key');

  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return;
  }

  const parsedUrl = url.parse(req.url, true);
  let pathname = parsedUrl.pathname;

  // 1. Ollama Proxy: /api/ollama/* -> http://127.0.0.1:11434/*
  if (pathname.startsWith('/api/ollama/')) {
    const targetPath = pathname.replace('/api/ollama', '') + (parsedUrl.search || '');
    
    const proxyReq = http.request({
      hostname: OLLAMA_HOST,
      port: OLLAMA_PORT,
      path: targetPath,
      method: req.method,
      headers: {
        ...req.headers,
        host: `${OLLAMA_HOST}:${OLLAMA_PORT}`
      }
    }, (proxyRes) => {
      res.writeHead(proxyRes.statusCode, proxyRes.headers);
      proxyRes.pipe(res);
    });

    proxyReq.on('error', (err) => {
      res.writeHead(502, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({
        error: `Could not connect to Ollama at http://${OLLAMA_HOST}:${OLLAMA_PORT}. Make sure Ollama daemon is running ('ollama serve').`,
        details: err.message
      }));
    });

    req.pipe(proxyReq);
    return;
  }

  // 2. Google Gemini API Proxy: /api/google/* -> https://generativelanguage.googleapis.com/*
  if (pathname.startsWith('/api/google/')) {
    const targetPath = pathname.replace('/api/google', '') + (parsedUrl.search || '');

    const proxyReq = https.request({
      hostname: 'generativelanguage.googleapis.com',
      port: 443,
      path: targetPath,
      method: req.method,
      headers: {
        ...req.headers,
        host: 'generativelanguage.googleapis.com'
      }
    }, (proxyRes) => {
      res.writeHead(proxyRes.statusCode, proxyRes.headers);
      proxyRes.pipe(res);
    });

    proxyReq.on('error', (err) => {
      res.writeHead(502, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ error: err.message }));
    });

    req.pipe(proxyReq);
    return;
  }

  // 3. Static File Server
  if (pathname === '/' || pathname === '') {
    pathname = '/index.html';
  }

  // Safe path resolution inside workspace root
  const safePath = path.normalize(path.join(__dirname, pathname));
  if (!safePath.startsWith(__dirname)) {
    res.writeHead(403, { 'Content-Type': 'text/plain' });
    res.end('Access Denied');
    return;
  }

  fs.stat(safePath, (err, stats) => {
    if (err || !stats.isFile()) {
      res.writeHead(404, { 'Content-Type': 'text/plain' });
      res.end('404 Not Found');
      return;
    }

    const ext = path.extname(safePath).toLowerCase();
    const contentType = MIME_TYPES[ext] || 'application/octet-stream';

    res.writeHead(200, {
      'Content-Type': contentType,
      'Content-Length': stats.size,
      'Cache-Control': 'no-cache'
    });

    const stream = fs.createReadStream(safePath);
    stream.pipe(res);
  });
});

server.listen(PORT, () => {
  console.log(`\n======================================================`);
  console.log(`  Gemma 4 Arena Workbench running at:`);
  console.log(`  Local: http://localhost:${PORT}`);
  console.log(`  Ollama Proxy: http://localhost:${PORT}/api/ollama`);
  console.log(`======================================================\n`);
});
