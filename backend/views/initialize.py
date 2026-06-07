import time
from pathlib import Path

import requests
from django.http import FileResponse, HttpResponse
from django.shortcuts import render
from django.conf import settings


def download_file(url: str, path: str) -> None:
    target_path = settings.KCS2_ASSETS_DIR / path
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
    new_path = request.path.lstrip("/")
    asset_path = settings.KCS2_ASSETS_DIR / new_path
    if not asset_path.is_file():
        if "resources/voice/kc" in new_path:
            real_path = new_path.replace("resources/voice", "sound")
            download_file(settings.KCS_BASE_URL + real_path, new_path)
        else:
            download_file(settings.KCS2_BASE_URL + new_path, new_path)

    if not asset_path.exists():
        return HttpResponse("Not Found", status=404)

    return FileResponse(open(asset_path, "rb"), content_type="application/octet-stream")


def favicon(request):
    return HttpResponse("", status=204)
