from flask import Flask
from typing import List, Union, Dict, Any, Type

Json = Union[List[Dict[str, Any]], Dict[str, Any]]

FlaskAppT = Type[Flask]