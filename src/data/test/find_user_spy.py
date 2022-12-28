from typing import Dict, List

from src.domain.models import Users
from src.domain.test import mock_users


class FindUserSpy:
    """class to define use case: Select User"""

    def __init__(self, user_repository: any):
        self.user_repository = user_repository
        self.by_id_params = {}
        self.by_name_params = {}
        self.by_id_and_name_params = {}

    def by_id(self, id: int) -> Dict[bool, List[Users]]:
        """Select a User by id
        Args:
            id (int): user id
        Returns:
            Dict[bool, List[Users]]: dictionary with information of the process
        """
        response = None
        self.by_id_params["id"] = id
        validation = isinstance(id, int)
        if validation:
            response = mock_users()

        return {"Success": validation, "Data": [response]}

    def by_name(self, name: str) -> Dict[bool, List[Users]]:
        """Select a User by name
        Args:
            name (str): user name
        Returns:
            Dict[bool, List[Users]]: dictionary with information of the process
        """
        response = None
        self.by_name_params["name"] = name
        validation = isinstance(name, str)
        if validation:
            response = mock_users()

        return {"Success": validation, "Data": [response]}

    def by_id_and_name(self, _id: int, name: str) -> Dict[bool, List[Users]]:
        """Select a User by id
        Args:
            id (int): user id
            name (str): user name
        Returns:
            Dict[bool, List[Users]]: dictionary with information of the process
        """
        response = None
        self.by_id_and_name_params["id"] = _id
        self.by_id_and_name_params["name"] = name
        validation = isinstance(_id, int) and isinstance(name, str)
        if validation:
            response = mock_users()

        return {"Success": validation, "Data": [response]}
