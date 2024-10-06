import socket
from handle_request import handle_request
from threading import Thread

# the constants are these 
#   PORT: int = 4444
#   HOST: str = "localhost"
#   CRLF: str = "\r\n"
#   HTTP_VERSION = "1.1"


def check_close(server: socket.socket) -> None:
    """
    Monitors for user input to gracefully shut down the server.

    Continuously checks for the 'q' key press. If 'q' is pressed, 
    the server socket is closed, and the program exits.

    Args:
        server (socket.socket): The server socket to be closed.
    """
    while True:
        if read_key() == "q":
            print("Quitting...")
            server.close()
            sys.exit(0)


def start_server():
    # Create a server socket
    server_socket = socket.create_server(("localhost", 4221), reuse_port=False)

    # Set the SO_REUSEADDR option
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.listen(5) 

    ################################################################
    # t1 = Thread(target=check_close, args=(server,))
    # t1.daemon = True  
    # t1.start()
    ################################################################

    print("Server is running on http://localhost:4221")

    while True:
        # Wait for a client connection
        client_socket, address = server_socket.accept()
        print(f"Connection from {address} has been established.")

        # Receive the request data
        request_data = client_socket.recv(1024).decode()
        print(f"Received request:\n{request_data}")
        
        # Handle the HTTP request and get the response
        response = handle_request(request_data)
        
        # Send the HTTP response back to the client
        client_socket.sendall(response.encode("utf-8"))
        
        # Close the client connection
        client_socket.close()


if __name__ == "__main__":
    start_server()
