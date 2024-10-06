def handle_request(data):
    """Parse the HTTP request and return a response."""

    lines = data.splitlines()  # Split the request into lines

    print(lines)

    request_line = lines[0]  # Get the request line (e.g., "GET / HTTP/1.1")

    print(request_line)

    # Parse the request line
    method, path, _ = request_line.split()

    print(method, path)
    
    # Handle different paths
    if path == "/":
        response_body = "Welcome to the HTTP Server!"
        status_code = "200 OK"
    elif path == "/hello":
        response_body = "Hello, World!"
        status_code = "200 OK"
    elif path.startswith("/echo/"):
        echo_string = path[len("/echo/"):]  # Get the string after "/echo/"
        response_body = echo_string
        status_code = "200 OK"
    else:
        response_body = "404 Not Found"
        status_code = "404 Not Found"
    
    # Create HTTP response
    response = f"HTTP/1.1 {status_code}\r\n"
    response += "Content-Type: text/plain\r\n"
    response += f"Content-Length: {len(response_body)}\r\n"
    response += "\r\n"  # End of headers
    response += response_body  # Body of the response
    
    return response