import { StrictMode } from 'react'
import { HashRouter, Routes, Route } from 'react-router-dom'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import Utils from './Utils.jsx'
import './index.css'

createRoot(document.getElementById('root')).render(
  <HashRouter>
    <Routes>
      {/* 原有的主页面 */}
      <Route path="/" element={<App />} />
      {/* 新增的测试页面 */}
      <Route path="/utils" element={<Utils />} />
    </Routes>
  </HashRouter>
)
