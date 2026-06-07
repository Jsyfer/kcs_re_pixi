import time
from pathlib import Path

import requests
from django.http import FileResponse, HttpResponse
from django.shortcuts import render

BASE_DIR = Path(__file__).resolve().parent.parent
KCS2_BASE_URL = "https://w02k.kancolle-server.com/kcs2/"
KCS_BASE_URL = "https://w02k.kancolle-server.com/kcs/"
KCS2_ASSETS_DIR = BASE_DIR / "assets" / "kcs2"
API_DIR = BASE_DIR / "api"


def download_file(url: str, path: str) -> None:
    target_path = KCS2_ASSETS_DIR / path
    target_path.parent.mkdir(parents=True, exist_ok=True)

    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        with open(target_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)


def create_response_from_file(filepath: Path) -> HttpResponse:
    if not filepath.exists():
        return HttpResponse("Not Found", status=404)

    body = filepath.read_text(encoding="utf-8").strip()
    if not body.startswith("svdata="):
        body = "svdata=" + body

    return HttpResponse(body, content_type="text/plain")


def index(request):
    return render(request, "index.html")


def send_assets(request, path: str):
    asset_path = KCS2_ASSETS_DIR / path
    if not asset_path.is_file():
        if "resources/voice/kc" in path:
            real_path = path.replace("resources/voice", "sound")
            download_file(KCS_BASE_URL + real_path, path)
        else:
            download_file(KCS2_BASE_URL + path, path)

    if not asset_path.exists():
        return HttpResponse("Not Found", status=404)

    return FileResponse(open(asset_path, "rb"), content_type="application/octet-stream")


def send_kcsapi(request, path: str):
    file_path = API_DIR / path
    if not file_path.is_file():
        return HttpResponse("Not Found", status=404)
    return FileResponse(open(file_path, "rb"), content_type="application/json")


def send_kcsapi_request(request, path: str):
    if request.method == "OPTIONS":
        return HttpResponse("", status=204)

    file_path = API_DIR / "kcsapi" / path
    return create_response_from_file(file_path)


def send_initial_loading(request):
    time.sleep(2.5)
    return HttpResponse('{"status": 200}', content_type="application/json")


def favicon(request):
    return HttpResponse("", status=204)
