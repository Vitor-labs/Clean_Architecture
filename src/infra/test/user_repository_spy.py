from typing import List

from src.domain.models import Users
from src.domain.test import mock_users


class UserRepositorySpy:
    """Spy to User Repository"""

    def __init__(self):
        self.insert_user_params = {}
        self.select_user_params = {}

    def insert_user(self, name: str, password: str) -> Users:
        """Spy to all atributes of insert method"""
        self.insert_user_params["name"] = name
        self.insert_user_params["password"] = password

        return mock_users()

    def select_user(self, id: int = None, username: str = None) -> List[Users]:
        """Spy to all atributes of select method"""
        self.select_user_params["id"] = id
        self.select_user_params["username"] = username

        return [mock_users()]
