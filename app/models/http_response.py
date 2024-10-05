from ftplib import CRLF
from constants import HTTP_VERSION


class HttpResponse:
    status_code: int
    content_type: str
    body: str

    def __init__(self, status_code: int, content_type: str, body: str = ""):
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


class HttpContentType:
    PLAIN_TEXT = "text / plain"
