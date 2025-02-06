from typing import Dict, Any, Final
from flask import Blueprint
from modules.api.v1 import api_v1
from modules.api.v1_1 import api_v1_1
from modules.api.v2 import api_v2

api = Blueprint(
    "api", __name__
)

V1      : Final = 'v1'
V1_1    : Final = 'v1.1'
V2      : Final = 'v2'

api.register_blueprint(api_v1, url_prefix=f"/{V1}")
api.register_blueprint(api_v1_1, url_prefix=f"/{V1_1}")
api.register_blueprint(api_v2, url_prefix=f"/{V2}")
