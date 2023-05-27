from typing import Dict, List

from src.domain.models import Pets, Users
from src.domain.test import mock_users, mock_pets


class RegisterPetSpy:
    """class to define use case: Register Pet"""
    def __init__(self, pet_repository: any, register_pet: any) -> None:
        self.pet_repository = pet_repository
        self.register_pet = register_pet
        self.registry_params = {}

    def registry(self, name: str, specie: str, user: Dict[int, str], age: int = None) -> Dict[bool, Pets]:
        """Resgistry a new Pet"""
        self.registry_params["name"] = name
        self.registry_params["specie"] = specie
        self.registry_params["user"] = user
        self.registry_params["age"] = age

        response = None

        # Validating entry and trying to find an user
        validate_entry = isinstance(name, str) and isinstance(specie, str)
        user = self.__find_user_information(user)
        checker = validate_entry and user["Success"]

        if checker:
            response = mock_pets()

        return {"Success": checker, "Data": response}

    @classmethod
    def __find_user_information(cls, user_information: Dict[int, str]) -> Dict[bool, List[Users]]:
        """ Check user information and selects user """

        user_founded = None
        user_params = user_information.keys()

        if "user_id" and "user_name" in user_params:
            # find user by id and name
            user_founded = {"Success": True, "Data": mock_users()}

        elif "user_name" not in user_params and "user_id" in user_params:
            # find user by id
            user_founded = {"Success": True, "Data": mock_users()}

        elif "user_id" not in user_params and "user_name" in user_params:
            # find user by name
            user_founded = {"Success": True, "Data": mock_users()}

        else:
            return {"Success": False, "Data": None}

        return user_founded
