from flask import Flask, render_template, send_from_directory
import time
import json

app = Flask(__name__, template_folder="dist", static_folder="dist/static")


# 渲染主页
@app.route("/")
def index():
    return render_template("index.html")


# 提供静态文件
@app.route("/kcs2/<path:path>")
def send_assets(path):
    return send_from_directory("kcs2", path)


# 初始化加载信息
@app.route("/initial_loading")
def send_initial_loading():
    time.sleep(2.5)
    return {"status": 200}


# kcsapi
@app.route("/kcsapi/api_start2/getData", methods=["GET"])
def api_start2_get_data():
    with open("src/kcsapi/api_start2/getData.json") as f:
        return json.load(f)


@app.route("/kcsapi/api_get_member/require_info", methods=["GET"])
def api_get_member_require_info():
    with open("src/kcsapi/api_get_member/require_info.json") as f:
        return json.load(f)


@app.route("/kcsapi/api_port/port", methods=["GET"])
def api_port_port():
    with open("src/kcsapi/api_port/port.json") as f:
        return json.load(f)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8000)
