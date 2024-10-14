import socket
from handle_request import handle_request
from handle_client import handle_client
from threading import Thread


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
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.listen(5) 
    print("Server is running on http://localhost:4221")

    while True:
        # Wait for a client connection
        client_socket, address = server_socket.accept()
        print(f"Connection from {address} has been established.")

        # Handle the client in a new thread
        client_thread = Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()


if __name__ == "__main__":
    start_server()
