import json
from enum import Enum
from typing import List, Tuple
from custom_types import Json

def initialize(app):

    with app.app_context():
        
        # we must keep the json at cloud file storage & read it here .
        with open('custom_server_codes.json', 'r+') as f:
            custom_server_code: Json = json.load(f)

        codes: List[str] = [ e["code"] for e in custom_server_code]

        if app.config["DEBUG"] == True:
            value: List[str] =  [e["code"] + "<" + e["message"] + ">" for e in custom_server_code]
        else:
            value: List[str] = codes

        code_isto_value : List[Tuple[str]] = tuple(zip(codes, value))
        ServerCodes: Enum = Enum('ServerCodes', code_isto_value, type=str)

        app.config["ServerCodes"] = ServerCodes
