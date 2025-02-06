"""Response Format and Formation util
"""
import json
from dataclasses import dataclass, field, asdict
from typing import List, Union, Dict, Any, Optional
from flask import Response
from custom_types import Json

__all__ = [
    'JsonApiResponse',
    'JsonErrorResponse'
]


def pagination_response_struct():
    """schmea of pagination parameters"""

    @dataclass
    class Page:
        total: int = 0
        current: Union[int, None] = None
        next: Union[int, None] = None
        prev: Union[int, None] = None
        link: dict = field(default_factory=lambda: {"next": None, "prev": None})

    return Page()


@dataclass
class JsonApiResponse:
    """schema of a json response type"""

    message: str = ""
    code: str = None
    data: Optional[Json] = None
    page: dict = field(default_factory=pagination_response_struct)
    http_status_code: Optional[int] = 200

    def make(self, paginated=False) -> Response:
        """makes a flask response"""

        _mimetype = "application/json"
        if not isinstance(self.data, (type(None), list, dict, tuple)):
            error_message = (
                f"JsonApiResponse<data> should be any of types : {[list, dict, tuple]}"
            )
            raise TypeError(error_message)

        response = dict(message=self.message, code=self.code, data=self.data)
        if paginated:
            response["page"] = asdict(self.page)
        json_response = json.dumps(response, default=str)
        return Response(
            response=json_response,
            status=self.http_status_code,
            mimetype=_mimetype,
        )

@dataclass
class JsonErrorResponse:
    """schema of a json response type"""

    message: str = ""
    code: Optional[str] = None
    errors: Optional[Json] = None
    http_status_code: Optional[int] = 400

    def make(self) -> Response:
        """makes a flask response"""

        _mimetype = "application/json"
        if not isinstance(self.errors, (type(None), list, dict, tuple)):
            error_message = (
                f"JsonErrorResponse<data> should be any of types : {[list, dict, tuple]}"
            )
            raise TypeError(error_message)

        response = dict(message=self.message, code=self.code, errors=self.errors)
        json_response = json.dumps(response, default=str)
        return Response(
            response=json_response,
            status=self.http_status_code,
            mimetype=_mimetype,
        )

"""How To Use :

# -- JsonApiResponse --

# get a response object . It's in a specified format.
response = JsonApiResponse()

# define/modify the response properties anywhere in api code .
response.http_status_code = 400
response.message : str = "some readable text"
response.code : str = "SOME_SECRET_CLIENT_DEFINED_CODE"
response.data : (dict,list,tuple) = "data"

# return response as when needed (preferably at the End) --
return response.make()

# include information of page in the response if desired .
return response.make(paginated=True)

# add pagination information (based on your pagination logic) .
page = response.page
page.current = 1
page.next = 2
page.total = do_calculate_total_pages()
page.link.next = request.baseurl + '?page=2 && page_size=15'

return response.make(paginated=True)

# -- xx --

"""
