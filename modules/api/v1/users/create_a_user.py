from flask import request
from modules.api.common import Api
from typing import TypedDict, Any, Dict, Optional
from typing_extensions import Self, NotRequired
from modules.api.models import User 
from modules.api.v1.services import DbService
from modules.api.v1.sql import sql_create_user
from exceptions import BadRequest
from flask import current_app
from pyutils.typecheck import TypeCheck
from dataclasses import dataclass

# TODO : automatic doc creation / swagger etc .

# :Custom Exception:TypeCheck Callback:
class ValidationFailed(Exception):

    def __init__(self, name, value, validation_name):
        self.name = name
        self.value = value
        self.validation_name = validation_name

    __str__ = lambda self: f"Invalid value for field - `{self.name}`"

# :Custom Exception:TypeCheck Callback:
class TypeCheckFailed(Exception):

    def __init__(self, name, current_type, expected_type):
        self.name = name
        self.current_type = current_type
        self.expected_type = expected_type

    __str__ = lambda self: f"Invalid Type for field - `{self.name}`, expected - `{self.expected_type}`, but got - `{self.current_type}`"

# :Custom Exception:
class RecordNotFound(Exception): ...


# :Schema:
@dataclass(frozen=True)
class RequestBodySchema(TypeCheck):

    username: str
    firstname: str
    lastname: str
    email: str
    created_by: int
    age : Optional[int] = None

    # Constants
    MAX_AGE = 25
    
    # Field Validators
    username_validator = lambda value: value.islower()
    firstname_validator = lastname_validator = lambda value: ' ' not in value
    age_validator = lambda value: value < RequestBodySchema.MAX_AGE if value else True

    # Exceptions
    validator_exception = ValidationFailed
    type_exception = TypeCheckFailed

    # Custom Methods
    def check_database__created_by(self, using_raw_cursor) -> None:
        is_exists = False
        with using_raw_cursor() as cur:
            result = cur.execute('SELECT EXISTS(SELECT 1 id from user where id=?);', (str(self.created_by)))
            is_exists = bool([v for v in result.fetchone()][0])
        
        if not is_exists:
            raise RecordNotFound("created_by")
        
        return is_exists

# :Custom Type:
class RequestBodyDict(TypedDict):
    """
    
    Tags: [Type | ...]
    """
    username: str
    firstname: str
    lastname: str
    email: str
    created_by: int
    age : NotRequired[int]

# :Custom Type:
class InsertedUserDict(RequestBodyDict):
    id: int


# :Api:
class CreateUser(Api):

    def __init__(self, logged_in_user: User, db_service: DbService):
        super().__init__()

        self.logged_in_user: User = logged_in_user
        self._db_service = db_service
        
    def _request_parsing(self: Self,) -> RequestBodyDict:
        """
        Http Request Parsing
        ====================


        """
        request_data: Dict[str, Any] = request.get_json()
        validated_data: RequestBodySchema = Validators.check_request_body(request_data, using_raw_cursor=self._db_service.using_raw_cursor)
        print(validated_data)
        data : RequestBodyDict = Validators.check_and_format_request_body_fields(validated_data)
        return data
    
    def _main_logic(self: Self, data: RequestBodyDict) -> InsertedUserDict:
        """
        Api Logic
        =========

        args:
            - data : RequestBodyDict | validated & parsed request body
        
        insert data in database using DbService
        """

        query = sql_create_user,\
                (data["username"], data["firstname"], data["lastname"], data["email"], data["age"], data["created_by"])
        inserted_id: int = self._db_service.insert_record(query)
        return {**{"id":inserted_id}, **data}

    def _response_formation(self, data: dict):
        """
        
        """
        return {"message": "user created", "data": data}, 201
    
    def execute(self: Self) -> Any:
        
        data: RequestBodyDict = self._request_parsing()
        data: Any = self._main_logic(data)
        return self._response_formation(data)

# :Api Validations:
class Validators:

    @staticmethod
    def check_request_body(data: Dict[str, Any], using_raw_cursor) -> RequestBodySchema:
        """
        verfying API request body
        """
        try:
            result = RequestBodySchema(**data)
            result.check_database__created_by(using_raw_cursor)
            return result
        except ValidationFailed as e:
            
            code = current_app.config["ServerCodes"].VALIDATE

            if e.validation_name == "username_validator":
                # "USERNAME_FORMAT_COMPLIANCE"     # you can store this in ServerCodes
                ... # e.g : code=current_app.config["ServerCodes"].USERNAME_FORMAT_COMPLIANCE
            if e.validation_name in ("firstname_validator", "lastname_validator"):
                # "NAME_FORMAT_COMPLIANCE"         # you can store these in ServerCodes
                ... # e.g : code=current_app.config["ServerCodes"].NAME_FORMAT_COMPLIANCE
            if e.validation_name == "age_validator":
                # "AGE_LIMIT_OFFSET"               # you can store these in ServerCodes
                ... # e.g : code=current_app.config["ServerCodes"].AGE_LIMIT_OFFSET

            raise BadRequest(
                custom_message=f"Invalid {e.name}",
                errors=[
                    str(e)
                ],
                code=code
            )
        except TypeCheckFailed as e:
            raise BadRequest(
                custom_message=f"Invalid {e.name}",
                errors=[
                    str(e)
                ],
                code=current_app.config["ServerCodes"].TYPE_ERR
            )
        except RecordNotFound as e:

            code = current_app.config["ServerCodes"].VALIDATE
            # "DB_404"     # you can store this in ServerCodes
            ... # e.g : code=current_app.config["ServerCodes"].DB_404
            raise BadRequest(
                custom_message=f"Invalid {e}",
                errors=[
                    "record not found"
                ],
                code=code
            )
        except Exception as e:
            raise e
    
    @staticmethod
    def check_and_format_request_body_fields(data: RequestBodySchema) -> RequestBodyDict:
        ...
        return data.__dict__


# == :Tags: == #
"""

:Cutsom Type:
    These are the types that are used within the code for 
        type hinting purpose and for static typecheckers .

:TypeCheck Callback:
    These are the callbacks ( classes / functions ) that
    are used within the pyutils.typecheck.TypeCheck based
    schema classes for handling the exceptions raised
    during the schema validations .

:Schema:
    Thses are the python classes that inherit 
    pyutils.typechec.TypeCheck class .

:Api:
    This will be an api implementation
    corresponding to a route specified 
    in the controller file .

:Api Validations:
    This will contain all the validation logic that will 
    be required within the :Api:
"""
# ==  :xx:  == #

