from ftplib import CRLF
from app.models.constants import HTTP_VERSION
from app.models.path import Path


class HttpContentType:
    PLAIN_TEXT: str = "text/plain"
    FILE: str = "application/octet-stream"


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
        return f"HTTP/{HTTP_VERSION} {self.status_code} {self.responses[self.status_code]}{CRLF} \
                Content-Type: {self.content_type}{CRLF} \
                Content-Length: {len(self.body)}{CRLF*2} \
                {self.body}".encode()

    responses: dict[int, str] = {
        100: "Continue",
        101: "Switching Protocols",
        200: "OK",
        201: "Created",
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
    accept: str
    content_type: str
    content_length: int

    def __init__(self, headers: list[str]):
        for header in headers:
            if len(header) < 2:
                continue
            header_elements = header.split(":")
            key, value = header_elements[0], header_elements[1].strip()
            match key:
                case "Host":
                    self.host = value
                case "User-Agent":
                    self.user_agent = value
                case "Accept":
                    self.accept = value
                case "Content-Type":
                    self.content_type = value
                case "Content-Length":
                    self.content_length = int(value)

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
    body: str

    def __init__(
        self, path: Path, method: str, http_version: str, headers: RequestHeaders, body: str = ''
    ) -> None:
        if method not in self.httpMethods:
            raise Exception(
                f"Method ${method} is not Valid\nValid Methods{self.httpMethods}"
            )
        self.path = path
        self.method = method
        self.http_version = http_version
        self.headers = headers
        self.body = body
