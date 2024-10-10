import os
from app.config import FILES_DIR
from app.models.http import HttpContentType, HttpRequest, HttpResponse

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


def hello(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        status_code=200,
        body='Hello World!'
    )
