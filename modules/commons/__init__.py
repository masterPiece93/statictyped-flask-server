from typing import Dict, Any
from flask import Blueprint


common_bp = Blueprint(
    "common_bp", __name__, template_folder="templates", static_folder="static"
)

@common_bp.route('/health')
def health() -> Dict[str, Any]:
    return {"healthy": True}

@common_bp.route('/docs')
def documentation() -> str:
    return """INDEX

    List Of Available API's :

        ...
    
    Api Documentation :

        ...
    
        
    """

