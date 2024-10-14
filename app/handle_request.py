import os
import sys

def handle_request(data):
    """Parse the HTTP request and return a response."""

    lines = data.splitlines()  # Split the request into lines

    print(lines)

    request_line = lines[0]  # Get the request line (e.g., "GET / HTTP/1.1")

    print(request_line)

    # Parse the request line
    method, path, _ = request_line.split()

    print(method, path)

    user_agent = None;
    for line in lines:
        if line.startswith("User-Agent:"):
            user_agent = line
            break

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
    elif path == "/user-agent":
        response_body = user_agent.split(" ")[1]
        status_code = "200 OK"
    elif path.startswith("/files/"):
        # Extract the filename from the path
        filename = path[len("/files/"):]
        file_path = os.path.join("static", filename)  # Files served from 'static' folder
        print(file_path)
        print(filename)

        # Handle POST request (create or overwrite a file)
        if method == "POST":
            # Find the start of the body in the raw HTTP data
            body_index = data.find("\r\n\r\n") + 4
            if body_index != -1:
                # Extract the body (text data)
                body = data[body_index:]

                # Write the body text to a new file in the 'static' folder
                with open(file_path, 'w') as file:
                    file.write(body)

                # Send success response
                response = "HTTP/1.1 201 Created\r\n"
                response += "Content-Type: text/plain\r\n"
                response += f"Content-Length: {len(body)}\r\n"
                response += "\r\n"
                response += "File created successfully!"

                return response

        # Handle GET request (read and return a file)
        elif method == "GET":
            # Check if the file exists
            if os.path.exists(file_path) and os.path.isfile(file_path):
                # Open and read the file in binary mode
                with open(file_path, 'rb') as file:
                    file_data = file.read()
                response = f"HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nContent-Length: {len(file_data)}\r\n\r\n{file_data}"
                # this doesn't work in Postman, but in the browser it does work by downloading it.
                return response 
            else:
                # Return 404 if file is not found
                response_body = "404 Not Found"
                status_code = "404 Not Found"

                # Create HTTP response for 404
                response = f"HTTP/1.1 {status_code}\r\n"
                response += "Content-Type: text/plain\r\n"
                response += f"Content-Length: {len(response_body)}\r\n"
                response += "\r\n"
                response += response_body

                return response
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