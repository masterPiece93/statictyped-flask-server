from custom_types import FlaskAppT
from werkzeug.exceptions import HTTPException
from exceptions import BadRequest
from api_reponse import *
# from custom_server_codes import ServerCodes
from typing import Type
from exceptions import ApiNotImplemented

def register(app: FlaskAppT):

    with app.app_context():
        ServerCodes = app.config["ServerCodes"]
        
        @app.errorhandler(BadRequest)
        def _bad_request_handler(bad_request_obj: BadRequest):
            """400(BAD REQUEST) Exception Handler"""

            _http_code_: int = 400
            _client_code_: Type[ServerCodes] = (
                bad_request_obj.code
                if bad_request_obj.code != None
                else ServerCodes.VALIDATE
            )
            response = JsonErrorResponse()
            response.message = bad_request_obj.message
            response.http_status_code = _http_code_
            response.code = _client_code_.value
            response.errors = bad_request_obj.errors

            return response.make()

        @app.errorhandler(ApiNotImplemented)
        def _un_implemented_handler(e: NotImplementedError):
            
            response5xx = JsonErrorResponse()
            _http_code_: int = 500
            response5xx.message = "Internal Server Serror"
            response5xx.code = "INTERNAL_ERR"
            response5xx.errors = ["Hint: Please Refer Logs - ID:"]

            if isinstance(e, ApiNotImplemented):
                _http_code_: int = 501
                response5xx.message = e.message
                response5xx.code = e.code
                response5xx.errors = []
            
            if _http_code_ == 500:
                # log it
                app.logger.error(e, exc_info=True)
                # stacktrace
                if app.config.get('DEBUG', False):
                    raise e
                
            response5xx.http_status_code = _http_code_
            return response5xx.make()
            
        @app.errorhandler(Exception)
        def _generatic_exceptions_handler(e: Exception):
            """Global Exception Handler for Python Exceptions"""

            if isinstance(e, HTTPException):
                # bypassing HTTP errors
                return e
            
            # for un-handled / code exceptions :
            app.logger.error(e, exc_info=True)
            if app.config.get('DEBUG', False):
                raise e
            _http_code_: int = 500
            response500 = JsonErrorResponse()
            response500.message = "Internal Server Serror"
            response500.http_status_code = _http_code_
            response500.code = "INTERNAL_ERR"
            response500.errors = ["Hint: Please Refer Logs - ID:"]
            return response500.make()
        