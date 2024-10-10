from concurrent.futures import ThreadPoolExecutor
import os

import requests
from app.models.constants import *
import socket

from app.models.constants import HOST, PORT


def test_stage_1():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")
        data: str = s.recv(1024).decode().lower()

        assert "HTTP/1.1 200 Ok".lower() in data
        assert "\r\n\r\n" in data


# * the function name must start with 'test' otherwise pytest will recognized as a normal func
def test_stage_2():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"GET /abcdefg HTTP/1.1\r\nHost: localhost\r\n\r\n")
        data: str = s.recv(1024).decode().lower()

        assert "HTTP/1.1 404 Not Found".lower() in data
        assert "\r\n\r\n" in data

def test_stage_3():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        test_message: str = 'abc'
        s.sendall(f"GET /echo/{test_message} HTTP/1.1\r\nHost: localhost\r\n\r\n".encode())

        data: str = s.recv(1024).decode().lower()

        assert "HTTP/1.1 200 ok".lower() in data
        assert str(len(test_message)) in data
        assert "abc".lower() in data
        assert "\r\n\r\n" in data


def test_stage_4():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        user_agent: str = "foobar/1.2.3"
        s.sendall(
            f"GET /user-agent HTTP/1.1\r\nHost: localhost\r\nUser-Agent: {user_agent}\r\nAccept: */*\r\n\r\n".encode()
        )

        data: str = s.recv(1024).decode().lower()

        assert "HTTP/1.1 200 ok".lower() in data
        assert str(len(user_agent)) in data
        assert user_agent.lower() in data
        assert "\r\n\r\n" in data


def test_stage_5():
    workers_count = 50 # concurrent request count
    with ThreadPoolExecutor(max_workers=workers_count) as executor:
        futures = [executor.submit(test_stage_4) for _ in range(workers_count)]
        for future in futures:
            future.result()  # Ensures exceptions are raised if any occur during the execution

def test_stage_6():
    FILES_DIR: str = "static" #! You must replaced if you chose another name
    FILENAME: str = "test"
    file_content: str = "Hello World\n"
    os.makedirs(FILES_DIR, exist_ok=True)
    filepath: str = f"{FILES_DIR}/{FILENAME}"
    with open(filepath, "w") as f:
        f.write(file_content)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(f"GET /files/{FILENAME} HTTP/1.1\r\nHost: localhost\r\n\r\n".encode())

        data: str = s.recv(1024).decode().lower()

        assert "HTTP/1.1 200 ok".lower() in data
        assert "application/octet-stream" in data
        assert str(len(file_content)) in data
        assert file_content.lower() in data
        assert "\r\n\r\n" in data


def test_stage_7():
    FILES_DIR: str = "static"  #! You must replaced if you chose another name
    FILENAME: str = "test"
    file_content: str = "Hello World\n"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(f"POST /files/{FILENAME} HTTP/1.1\r\nHost: localhost\r\n\r\n{file_content}".encode())

        data: str = s.recv(1024).decode().lower()

        assert "HTTP/1.1 201 Created".lower() in data
        
        os.makedirs(FILES_DIR, exist_ok=True)
        filepath: str = f"{FILES_DIR}/{FILENAME}"
        with open(filepath, "r") as f:
            assert f.read() == file_content

def test_get_request():
    response = requests.get(f"http://{HOST}:{PORT}")
    assert response.status_code == 200
