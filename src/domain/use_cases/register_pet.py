from abc import ABC, abstractclassmethod
from typing import Dict

from src.domain.models import Pets


class RegisterPet(ABC):
    """Interface to use case: Register Pet"""

    @abstractclassmethod
    def registry(
        cls, name: str, specie: str, user: Dict[int, str], age: int = None
    ) -> Dict[bool, Pets]:
        """Registry Use Case"""
        raise NotImplementedError("RegisterPet.registry() is not implemented")
