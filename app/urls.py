from app.views import *
from app.models.http import Path


paths: list[Path] = [
    Path("/", view=home_view),
    Path("/echo/{str}", view=echo_view),
    Path("/user-agent", view=get_user_agent),
    Path("/hello", view=hello),
    Path("/files/{str}", view=handle_files),
    Path("/json-test", view=json_test),
    Path("/img", view=img)
]
