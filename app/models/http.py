from ftplib import CRLF
from models.constants import HTTP_VERSION
from models.path import Path


class HttpContentType:
    PLAIN_TEXT: str = "text / plain"


class HttpResponse:
    status_code: int
    content_type: str
    body: str

    def __init__(
        self,
        status_code: int,
        content_type: str = HttpContentType.PLAIN_TEXT,
        body: str = "",
    ):
        self.status_code = status_code
        self.content_type = content_type
        self.body = body

    def serialize(self) -> bytes:
        return f"HTTP/{HTTP_VERSION} {self.status_code} {self.responses[self.status_code]}{CRLF}Content-Type: {self.content_type}{CRLF}Content-Length: {len(self.body)}{CRLF*2}{self.body}".encode()

    responses: dict[int, str] = {
        100: "Continue",
        101: "Switching Protocols",
        200: "OK",
        400: "Bad Request",
        401: "Unauthorized",
        404: "Not Found",
        500: "Internal Server Error",
        501: "Not Implemented",
        502: "Bad Gateway",
    }


class RequestHeaders:
    host: str
    user_agent: str

    def __init__(self, headers: list[str]):
        header_len = len(headers)
        print(headers)
        if header_len > 0:
            self.host = headers[0].split(" ")[1]
        if header_len > 1 and len(headers[1]) > 0:
            self.user_agent = headers[1].split(" ")[1]

    def __str__(self) -> str:
        return f"host {self.host} user agent {self.user_agent}"


class HttpRequest:
    httpMethods: list[str] = [
        "GET",
        "POST",
        "DELETE",
        "PUT",
        "UPDATE",
        "PATCH",
        "OPTIONS",
        "HEAD",
        "CONNECT",
        "TRACE",
    ]
    path: Path
    method: str
    http_version: str
    headers: RequestHeaders

    def __init__(
        self, path: Path, method: str, http_version: str, headers: RequestHeaders
    ) -> None:
        if method not in self.httpMethods:
            raise Exception(
                f"Method ${method} is not Valid\nValid Methods{self.httpMethods}"
            )
        self.path = path
        self.method = method
        self.http_version = http_version
        self.headers = headers
