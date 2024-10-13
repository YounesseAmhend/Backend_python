import os
from app.config import FILES_DIR
from app.models.http import HttpContentType, HttpRequest, HttpResponse
from app.models.utils import json_response, render_file

def home_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse(status_code=200)

def echo_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        status_code=200,
        body=request.path.value,
    )


def get_user_agent(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        status_code=200,
        body=request.headers.user_agent,        
    )


def handle_files(request: HttpRequest) -> HttpResponse:
    filename = request.path.value
    filepath = f"{FILES_DIR}/{filename}"
    print(f"FilePath {filepath}")
    if request.method == "GET":
        if not os.path.exists(filepath):
            return HttpResponse(
                status_code=404,
            )
        else:
            filedata: str
            with open(filepath, "r") as f:
                filedata = f.read()
            return HttpResponse(
                status_code=200,
                content_type=HttpContentType.FILE,
                body=filedata,
            )

    elif request.method == "POST":
        os.makedirs(FILES_DIR, exist_ok=True)
        with open(filepath, "w") as f:
            f.write(request.body)
        print("Sending")
        return HttpResponse(
            status_code=201,
        )
    else:
        return HttpResponse(status_code=501)

def hello(request: HttpRequest) -> HttpResponse:
    return render_file("hello.html")


def json_test(request: HttpRequest) -> HttpResponse:
    return json_response(
        {
            "age": 24,
            "name": "name",
        }
    )

def img(request: HttpRequest)->HttpResponse:
    return render_file(
        filename="img.png"
    )