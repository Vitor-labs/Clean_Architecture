from typing import Dict, List, Type

from src.domain.models import Pets
from src.domain.use_cases import FindPet as FindPetInterface
from src.data.interfaces import PetRepositoryInterface as PetRepository


class FindPet(FindPetInterface):
    """Class to define Find Pet use case"""

    def __init__(self, pet_repository: Type[PetRepository]):
        self.pet_repository = pet_repository

    def by_id(self, id: int) -> Dict[bool, List[Pets]]:
        """Select pet by id
        Args:
            id (int): id of the pet
        Returns:
            Dict[bool, List[Pets]]: Dictionary with information of the process
        """
        validate_entry = isinstance(id, int)
        response = None

        if validate_entry:
            response = self.pet_repository.select_pet(id=id)

        return {"Success": validate_entry, "Data": response}

    def by_user_id(self, user_id: int) -> Dict[bool, List[Pets]]:
        """Select pet by user id
        Args:
            user_id (int): id of the owner of the pet
        Returns:
            Dict[bool, List[Pets]]: Dictionary with information of the process
        """
        validate_entry = isinstance(user_id, int)
        response = None

        if validate_entry:
            response = self.pet_repository.select_pet(user_id=user_id)

        return {"Success": validate_entry, "Data": response}

    def by_id_and_user_id(self, id: int, user_id: int) -> Dict[bool, List[Pets]]:
        """Select pet by id and user id
        Args:
            id (int): id of the pet
            user_id (int): id of the owner of the pet
        Returns:
            Dict[bool, List[Pets]]: Dictionary with information of the process
        """
        validate_entry = isinstance(id, int) and isinstance(user_id, int)
        response = None

        if validate_entry:
            response = self.pet_repository.select_pet(id=id, user_id=user_id)

        return {"Success": validate_entry, "Data": response}
