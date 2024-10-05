


from views import echo_view
from models.path import Path


paths: list[Path] = [
    Path("/",),
    Path("/echo/{str}", func=echo_view),
]
