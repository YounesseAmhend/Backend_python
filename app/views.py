from models.http_response import HttpContentType, HttpResponse
from models.path import Path


def echo_view(path: Path) -> HttpResponse:
    return HttpResponse(
        status_code=200,
        content_type=HttpContentType.PLAIN_TEXT,
        body=path.value,
    )
