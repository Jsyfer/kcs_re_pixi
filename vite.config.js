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
  }
})
