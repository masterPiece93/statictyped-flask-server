from typing import Any
from flask import Blueprint


auth_bp = Blueprint(
    "auth_bp", __name__, template_folder="templates", static_folder="static"
)

@auth_bp.route('/')
def authentication_page() -> Any:
    return """
    Login:
        ...

    Signup:
        ...
    """