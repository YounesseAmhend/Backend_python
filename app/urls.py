from views import *
from models.http import Path


paths: list[Path] = [
    Path("/", view=home_view),
    Path("/echo/{str}", view=echo_view),
    Path("/user-agent", view=get_user_agent),
]
