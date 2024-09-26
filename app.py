from flask import Flask, render_template, send_from_directory
import time

app = Flask(__name__, template_folder='dist', static_folder='dist/static')

# 渲染主页
@app.route('/')
def index():
    return render_template('index.html')

# 提供静态文件
@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('assets', path)

# 初始化加载信息
@app.route('/initial_loading')
def send_initial_loading():
    time.sleep(2.5)
    return {'status': 200}

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)
