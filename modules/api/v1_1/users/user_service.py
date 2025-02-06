from typing import Any

class DbService:

    @staticmethod
    def get_user_by_id(user_id: int) -> Any:
        return dict(
            name="",
            age="",
            email="",
            address="",
            contact_numbers=[],
            functional_area=""
        )

    @staticmethod
    def check_id_exist_in_db(id: int) -> bool:
        ...
        return True