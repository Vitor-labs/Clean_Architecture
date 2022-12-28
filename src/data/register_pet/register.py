from typing import List, Type, Dict

from src.domain.use_cases import RegisterPet as RegisterPetInterface
from src.domain.models import Users, Pets
from src.data.interfaces import PetRepositoryInterface as PetRepository
from src.data.find_user import FindUser


class RegisterPet(RegisterPetInterface):
    """Class to define use case: Register Pet"""

    def __init__(self, pet_repository: Type[PetRepository], find_user: Type[FindUser]):
        self.pet_repository = pet_repository
        self.find_user = find_user

    def registry(
        self, name: str, specie: str, user: Dict[int, str], age: int = None
    ) -> Dict[bool, Pets]:
        """Registry a new Pet
        Args:
            name (str): name of the pet
            specie (str): specie of the pet
            user (Dict[int, str]): dictionary with owner id or/and owner name
            age (int, optional): age of the pet. Defaults to None.
        Returns:
            Dict[bool, Pets]: dictionary with information of the process
        """
        response = None

        validation = isinstance(name, str) and isinstance(specie, str)
        user_found = self.__find_user_info(user)
        checkout = validation and user_found["Success"]
        _id = user_found.get("id")

        if checkout:
            response = self.pet_repository.insert_pet(name, specie, age, _id)
        return {"Success": checkout, "Data": response}

    def __find_user_info(self, user_info: Dict[int, str]) -> Dict[bool, List[Users]]:
        """Checkout of user information and select him
        Args:
            user_info (Dict[int, str]): dictionary with user id or/and user name
        Returns:
            Dict[bool, List[Users]]: dictionary with information of the process and the response of use case: FindUser
        """
        user_founded = None
        attrs = user_info.keys()

        if "id" in attrs and "name" in attrs:
            user_founded = self.find_user.by_id_and_name(
                user_info["id"], user_info["name"]
            )

        elif "id" not in attrs and "name" in attrs:
            user_founded = self.find_user.by_name(user_info["name"])

        elif "id" in attrs and "name" not in attrs:
            user_founded = self.find_user.by_id(user_info["id"])

        else:
            return {"Success": False, "Data": None}

        return user_founded
