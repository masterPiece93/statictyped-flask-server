from abc import ABC, abstractmethod
from typing_extensions import Self, Any

class Api(ABC):

    @abstractmethod
    def _request_parsing(self: Self, *args: Any, **kwargs: Any) -> Any:
        """HTTP request parsing 
        
        - validating inputs ( params , headers, body)
        - formatting and perparing data for main processing

        [Private]
        """
        ...

    @abstractmethod
    def _main_logic(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Core Api Logic

        [Private]
        """
        ...

    @abstractmethod
    def _response_formation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """HTTP response

        [Private]
        """
        ...

    def execute(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Execute the api

        - _request_parsing
        - _main_logic
        - _response_formation
        
        [Public]
        """
