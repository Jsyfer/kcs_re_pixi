import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  build: {
    assetsDir: 'static',
    rollupOptions: {
      output: {
        entryFileNames: 'static/index.js',
        assetFileNames: 'static/index.[ext]'
      }
    }
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
      '@common': path.resolve(__dirname, 'src/common'),
      '@loading': path.resolve(__dirname, 'src/loading'),
      '@scene': path.resolve(__dirname, 'src/scene'),
      '@ship': path.resolve(__dirname, 'src/ship'),
    }
  },
  server: {
    host: true,
    port: 3000,
    proxy: {
      "/kcsapi": {
        target: "http://127.0.0.1:8000",
        changeOrigin: true,
        secure: false
      },
      "/kcs2": {
        // target: "http://203.104.209.87",
        target: "http://127.0.0.1:3000/assets",
        changeOrigin: true,
        secure: false
      }
    }
  }
})
