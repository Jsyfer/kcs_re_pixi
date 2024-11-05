import subprocess
import json
import shutil
import os

# build
subprocess.run(["npm", "run", "build"])

# copy build result to docs
os.makedirs("docs/static", exist_ok=True)
shutil.copyfile("dist/static/index.js", "docs/static/index.js")
shutil.copyfile("dist/static/index.ico", "docs/static/index.ico")
shutil.copyfile("dist/static/index.css", "docs/static/index.css")

# copy target assets to docs
with open("src/resources.json") as f:
    data = json.load(f)
    for item in data["assets"]:
        os.makedirs(os.path.dirname(os.path.join("docs", item)), exist_ok=True)
        shutil.copyfile(item, os.path.join("docs", item))
