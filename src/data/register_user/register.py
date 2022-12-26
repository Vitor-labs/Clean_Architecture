from typing import Dict, Type

from src.data.interfaces import UserRepositoryInterface as UserRepository
from src.domain.models.users import Users
from src.domain.use_cases import RegisterUser as RegisterUserInterface


class RegisterUser(RegisterUserInterface):
    """Class to define use case: Register User"""

    def __init__(self, user_repository: Type[UserRepository]):
        self.user_repository = user_repository

    def register(self, name: str, password: str) -> Dict[bool, Users]:
        """Register User use case
        :param - name: The name of the user
               - password: The password of the user
        :return: Dict with process information
        """
        # Validation protection to insertion
        validate_fields = isinstance(name, str) and isinstance(password, str)
        response = None

        if validate_fields:
            response = self.user_repository.insert_user(name, password)

        return {"Success": validate_fields, "Data": response}
