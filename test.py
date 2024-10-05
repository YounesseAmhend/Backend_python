import pytest, requests
from app.constants import *
import socket

from app.constants import HOST, PORT


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


# def test_get_request():
#     response = requests.get(f"http://{HOST}:{PORT}")
#     assert response.status_code == 200
