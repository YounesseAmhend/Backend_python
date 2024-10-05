class Path:
    path: str
    type: str | None

    def __init__(self, path: str, type: str | None = None):
        self.type = type
        self.path = path

paths: list[Path] = [
    Path("/"),
    Path("/echo", type="str"),
]
