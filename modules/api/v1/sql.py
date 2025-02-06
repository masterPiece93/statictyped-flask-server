"""
Contain Sql used in api's
"""

from typing import Final

sql_create_user : Final[str] = """
INSERT INTO user (username, firstname, lastname, email, age, created_by) VALUES (?, ?, ?, ?, ?, ?)
"""
