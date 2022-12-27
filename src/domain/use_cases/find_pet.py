from abc import ABC, abstractclassmethod
from typing import Dict, List

from src.domain.models import Pets


class FindPet(ABC):
    """Interface to FindPet use case"""

    @abstractclassmethod
    def by_id(self, id: int) -> Dict[bool, List[Pets]]:
        """Case by ID"""
        raise NotImplementedError("FindPet.by_id() is not implemented")

    @abstractclassmethod
    def by_user_id(self, user_id: int) -> Dict[bool, List[Pets]]:
        """Case by User ID"""
        raise NotImplementedError("FindPet.by_user_id() is not implemented")

    @abstractclassmethod
    def by_id_and_user_id(
        self, id: int, name: str, user_id: int
    ) -> Dict[bool, List[Pets]]:
        """Case by ID and User ID"""
        raise NotImplementedError("FindPet.by_id_and_user_id() is not implemented")
