import signal
import socket
from constants import *
from threading import Thread
from keyboard import read_key
import sys
from path import paths

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
            with client:
                data: str = client.recv(1024).decode()
                if not data:
                    break

                path = data.split(CRLF)[0].split(' ')[1]
                
                str_paths = map(lambda p: p.path , paths)
                if path in str_paths:
                    client.send(HttpResponse.OK.encode())
                elif path.split("/").pop(-1).join("/") in str_paths:
                    ...
                else: 
                    client.send(HttpResponse.NOT_FOUND.encode())  
                


if __name__ == "__main__":
    main()
