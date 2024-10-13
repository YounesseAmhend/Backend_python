import json
import os

from app.config import FILES_DIR
from app.models.http import HttpContentType, HttpResponse


import os


def render_file(filename: str) -> HttpResponse:
    filepath = f"{FILES_DIR}/{filename}"
    extension = os.path.splitext(filepath)[1].lower()

    try:
        match extension:
            case ".html":
                with open(filepath, "r") as f:
                    file_content = f.read()
                return HttpResponse(
                    status_code=200,
                    body=file_content,
                    content_type=HttpContentType.HTML,
                )

            case ".png":
                with open(filepath, "rb") as img_file:
                    img_bytes = img_file.read()
                return HttpResponse(
                    status_code=200, body=img_bytes, content_type=HttpContentType.PNG
                )

            case ".jpg" | ".jpeg":
                with open(filepath, "rb") as img_file:
                    img_bytes = img_file.read()
                return HttpResponse(
                    status_code=200, body=img_bytes, content_type=HttpContentType.JPEG
                )

            case ".gif":
                with open(filepath, "rb") as img_file:
                    img_bytes = img_file.read()
                return HttpResponse(
                    status_code=200, body=img_bytes, content_type=HttpContentType.GIF
                )

            case ".pdf":
                with open(filepath, "rb") as pdf_file:
                    pdf_bytes = pdf_file.read()
                return HttpResponse(
                    status_code=200, body=pdf_bytes, content_type=HttpContentType.PDF
                )

            case ".zip":
                with open(filepath, "rb") as zip_file:
                    zip_bytes = zip_file.read()
                return HttpResponse(
                    status_code=200, body=zip_bytes, content_type=HttpContentType.ZIP
                )

            case ".csv":
                with open(filepath, "r") as csv_file:
                    csv_content = csv_file.read()
                return HttpResponse(
                    status_code=200, body=csv_content, content_type=HttpContentType.CSV
                )

            case ".js":
                with open(filepath, "r") as js_file:
                    js_content = js_file.read()
                return HttpResponse(
                    status_code=200,
                    body=js_content,
                    content_type=HttpContentType.JAVASCRIPT,
                )

            case ".css":
                with open(filepath, "r") as css_file:
                    css_content = css_file.read()
                return HttpResponse(
                    status_code=200, body=css_content, content_type=HttpContentType.CSS
                )

            case _:
                with open(filepath, "rb") as default_file:
                    file_bytes = default_file.read()
                return HttpResponse(
                    status_code=200, body=file_bytes, content_type=HttpContentType.FILE
                )

    except FileNotFoundError:
        raise Exception(f"{extension.upper()} file not found: {filepath}")
    except Exception as e:
        raise Exception(f"Error processing the file: {str(e)}")

    raise Exception(f"File format {extension} is not supported.")


def json_response(value: dict):
    return HttpResponse(
        status_code=200,
        body=json.dumps(value),
        content_type=HttpContentType.JSON,
    )


def send_png(filename: str):
    filepath = f"{FILES_DIR}/{filename}"
