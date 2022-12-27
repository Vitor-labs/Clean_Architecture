from typing import Dict, List, Type

from src.domain.models import Users
from src.domain.use_cases import FindUser as FindUserInterface
from src.data.interfaces import UserRepositoryInterface as UserRepository


class FindUser(FindUserInterface):
    """Class to define Find User use case"""

    def __init__(self, user_repository: Type[UserRepository]):
        self.user_repository = user_repository

    def by_id(self, id: int) -> Dict[bool, List[Users]]:
        """Select user by id
        Args:
            id (int): id of the user
        Returns:
            Dict[bool, List[Users]]: Dictionary with information of the process
        """
        validate_entry = isinstance(id, int)
        response = None

        if validate_entry:
            response = self.user_repository.select_user(id=id)

        return {"Success": validate_entry, "Data": response}

    def by_name(self, name: str) -> Dict[bool, List[Users]]:
        """Select user by id
        Args:
            name (str): name of the user
        Returns:
            Dict[bool, List[Users]]: Dictionary with information of the process
        """
        validate_entry = isinstance(name, str)
        response = None

        if validate_entry:
            response = self.user_repository.select_user(name=name)

        return {"Success": validate_entry, "Data": response}

    def by_id_and_name(self, id: int, name: str) -> Dict[bool, List[Users]]:
        """Select user by id
        Args:
            id (int): id of the user
            name (str): name of the user
        Returns:
            Dict[bool, List[Users]]: Dictionary with information of the process
        """
        validate_entry = isinstance(id, int) and isinstance(name, str)
        response = None

        if validate_entry:
            response = self.user_repository.select_user(id=id, name=name)

        return {"Success": validate_entry, "Data": response}
