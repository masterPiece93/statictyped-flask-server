"""
Controller
"""
from typing import Dict, Optional
from flask import Blueprint
from typing import Any
from modules.api.v1.users.create_a_user import CreateUser as CreateUserApi
from flask import request
from db import get_db
from modules.api.v1.services import DbService
from exceptions import ApiNotImplemented

api_v1 = Blueprint("api_v1", __name__)

ImmutableDict = Dict


def get_logged_in_user() -> ImmutableDict[str, Any]:

    db = get_db()
    cur = db.cursor()

    cur.execute("SELECT * FROM `user` WHERE id=2")
    row = cur.fetchone()

    cur.close()
    db.commit()

    return dict(row) if row else None

# routes and controllers for routes

@api_v1.route('/user', methods=['GET', 'POST'])
@api_v1.route('/user/<string:user_id>', methods=['GET', 'PUT'])
def users_api_controller(user_id: Optional[str] = None) -> Any:

    loggerd_in_user = get_logged_in_user()
    db_service: DbService = DbService(db=get_db())

    if request.method == 'POST':
        return CreateUserApi(loggerd_in_user, db_service).execute()

    raise ApiNotImplemented()
