import os
from flask import Flask, render_template, send_from_directory
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# 渲染主页
@app.route('/')
@cross_origin()
def index():
    return render_template('index.html')


# 提供静态文件
@app.route('/assets/<path:path>')
@cross_origin()
def send_assets(path):
    return send_from_directory(os.path.join(app.root_path, 'assets'), path)


@app.route('/dist/<path:path>')
def send_dist(path):
    return send_from_directory(os.path.join(app.root_path, 'dist'), path)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)
