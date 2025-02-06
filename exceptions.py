"""Application exceptions
"""
from typing import Any, List, Optional
from enum import Enum

__all__ = [
    'UserPermissionDenied',
    'BadRequest',
    'NotFound',
    'ApiNotImplemented'
]


class UserPermissionDenied(Exception):
    def __init__(self, errors=[dict()], custom_message=None, code=None):
        self.http_status_code: int = 403
        self.code: Optional[Enum] = code
        self.errors: List[Any] = errors
        if custom_message:
            self.message: str = custom_message
        else:
            self.message: str = "User not allowed to perform this action"
        super().__init__(self.message)


class BadRequest(Exception):
    def __init__(self, errors=[dict()], custom_message: Optional[str] = None, code: Optional[Enum] = None):
        self.http_status_code: int = 400
        self.code: Optional[Enum] = code
        self.errors: List[Any] = errors
        if custom_message:
            self.message: str = custom_message
        else:
            self.message: str = "Invalid Api Request"
        super().__init__(self.message)


class NotFound(Exception):
    def __init__(self, custom_message=None):
        self.http_status_code: int = 404
        self.message: str = "Resouce Not Found"
        self.code: Optional[Enum] = None
        if custom_message:
            self.message = self.message + " | " + custom_message
        super().__init__(self.message)


class ApiNotImplemented(NotImplementedError):
    def __init__(self, custom_message=None):
        self.http_status_code: int = 501
        self.message: str = "Api Not Implemented"
        self.code: Optional[Enum] = None
        if custom_message:
            self.message = self.message + " | " + custom_message
        super().__init__(self.message)

