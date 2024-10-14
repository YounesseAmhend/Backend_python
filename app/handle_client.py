from handle_request import handle_request

def handle_client(client_socket , address):
    """
        Handles the incoming client connection.
        Receives request data, processes it, and sends a response.
        Args:
            client_socket (socket.socket): The socket for client communication.
            address (tuple): The client address.
    """
    print(f"Connection from {address} has been established.")

    try:
        # Receive the request data
        request_data = client_socket.recv(1024).decode()
        print(f"Received request from {address}:\n{request_data}")

        # Handle the HTTP request and get the response
        response = handle_request(request_data)

        # Send the HTTP response back to the client
        client_socket.sendall(response.encode("utf-8"))
    except Exception as e:
        print(f"Error handling request from {address}: {e}")
    finally:
        # Close the client connection
        client_socket.close()
        print(f"Connection closed with {address}")