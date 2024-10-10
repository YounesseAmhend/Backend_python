import sys
import socket
import threading
from app.models.http import *
from app.models.constants import *
from threading import Thread
from keyboard import read_key
from app.urls import paths

def check_close(server: socket.socket) -> None:
    """Continuously check for 'q' to quit the server."""
    while True:
        if read_key() == "q":
            print("Quitting...")
            server.close()
            sys.exit(0)


def main():
    # Create a server socket
    with socket.create_server((HOST, PORT), family=socket.AF_INET) as server:
        print(f"Running on http://{HOST}:{PORT}")
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.listen(1)

        t1 = Thread(target=check_close, args=(server,))
        t1.daemon = True  
        t1.start()
        while True:
            client, _ = server.accept()  
            threading.Thread(target=handleRequest, args=(client,)).start()


def handleRequest(client: socket.socket):
    with client:
        data: str = client.recv(1024).decode()

        request_str = data.split(CRLF)
        request_line = request_str[0].split(" ")
        path_value = request_line[1]

        headersBody = data.split(CRLF)[1:] 

        httpResponse: HttpResponse | None = None
        for path in paths:
            if path.match(path_value):
                method = request_line[0]
                http_version = request_line[2]
                request_headers = RequestHeaders(headers=headersBody)
                request = HttpRequest(
                        path=path,
                        method=method,
                        http_version=http_version,
                        headers=request_headers,
                    )
                httpResponse = path.func(request)
        if httpResponse == None: # This means the path does not exists
            httpResponse = HttpResponse(
                    status_code=404, content_type=HttpContentType.PLAIN_TEXT
                )
        client.send(httpResponse.serialize())


if __name__ == "__main__":
    main()
