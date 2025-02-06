from flask import request
from modules.api.common import Api
from typing import TypedDict, NoReturn, Any, Dict
from typing_extensions import Self

from .user_service import DbService

class User(TypedDict):
    name: str
    email: str

class GetUser(Api):

    def __init__(self: Self, user_id: str, db_service: DbService = DbService()) -> None:
        self._user_id = user_id
        self._db_service = db_service

    def _request_parsing(self) -> None:

        self._db_service.check_id_exist_in_db(self._user_id)
    
    def _main_logic(self: Self,) -> dict:
        
        user: Dict[Any, Any] = self._db_service.get_user_by_id(self._user_id)
        
        return user
    
    def _response_formation(self: Self, user: dict) -> dict:

        data: User = {
            "name": user["name"],
            "email": user["email"]
        }

        return {"message": "successful", "data": data}, 200 
    
    def execute(self: Self) -> dict:
        
        self._request_parsing()
        user: dict = self._main_logic()
        return self._response_formation(user)


