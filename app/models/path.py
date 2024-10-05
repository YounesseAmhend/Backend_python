from typing import Any, Callable

from models.http_response import HttpResponse


class Path:
    path: str
    value: Any = None
    func: Callable[[Any], HttpResponse] | None #Any will be in the future HttpRequest

    def __init__(self, path: str, func: Callable | None = None):
        self.path = path
        self.func = func

    def match(self, request_path: str) -> bool:
        path_parts = self.path.split("/")
        request_parts = request_path.split("/")

        if len(path_parts) != len(request_parts):
            return False

        for path_part, request_part in zip(path_parts, request_parts):
            if path_part.startswith("{") and path_part.endswith("}"):
                type: str = path_part[1:-1]
                match type:
                    case "str":
                        self.value = request_part
                    case "float":
                        self.value = float(request_part)
                    case "int":
                        self.value = int(request_part)

            elif path_part != request_part:
                return False
        
        return True
