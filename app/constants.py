PORT: int = 4444
HOST: str = "localhost"
CRLF: str = "\r\n"
HTTP_VERSION = "HTTP/1.1"

class HttpResponse :
    OK: str = f"{HTTP_VERSION} 200 OK{CRLF*2}"
    NOT_FOUND: str = f"{HTTP_VERSION} 404 Not Found{CRLF*2}"
    
    #* status code
    responses: dict[int, str] = {
        100: "Continue",
        101 :'Switching Protocols',
        200: "OK",
        400: 'Bad Request',
        401: "Unauthorized",
        404: "Not Found",
        500: "Internal Server Error",
        501: "Not Implemented",
        502: "Bad Gateway",
    }
    
    
