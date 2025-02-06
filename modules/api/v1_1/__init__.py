from typing import Union
from flask import Blueprint, request
from modules.api.v1.users.create_a_user import CreateUser as CreateUserV1
from modules.api.v1_1.users.get_a_user import GetUser as GetUser

api_v1_1 = Blueprint("api_v1_1", __name__)

@api_v1_1.route('/users', methods=['GET', 'POST'])
@api_v1_1.route('/users/<string:user_id>', methods=['GET', 'POST'])
def users_api_controller(user_id: Union[str, None] = None):
    
    if request.method == 'POST':
        CreateUserV1().execute()

    if user_id and request.method == "GET":
        GetUser(user_id)

    raise NotImplementedError("API Not Implemented Yet")
