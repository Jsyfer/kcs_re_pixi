import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

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
  server: {
    host: true,
    port: 3000,
    proxy: {
      "api": {
        target: "http://127.0.0.1:5000",
        changeOrigin: true,
        secure: false
      }
    }
  }
})
