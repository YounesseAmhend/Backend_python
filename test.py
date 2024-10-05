import pytest, requests
from app.constants import *
import socket

from app.constants import HOST, PORT


def test_stage_1():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")
        data: str = s.recv(1024).decode()

        assert "HTTP/1.1 200 OK\r\n\r\n".lower() in data.lower()

#* the function name must start with 'test' otherwise pytest will recognized as a normal func 
def test_stage_2():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"GET /abcdefg HTTP/1.1\r\nHost: localhost\r\n\r\n")
        data: str = s.recv(1024).decode()

        assert "HTTP/1.1 404 Not Found\r\n\r\n".lower() in data.lower()


# def test_get_request():
#     response = requests.get(f"http://{HOST}:{PORT}")
#     assert response.status_code == 200
