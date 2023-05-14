from abc import ABCMeta, abstractmethod
from typing import Dict

from src.domain.models import Pets


class RegisterPet(metaclass=ABCMeta):
    """Interface to use case: Register Pet"""

    @classmethod
    @abstractmethod
    def registry(
        cls, name: str, specie: str, user: Dict[int, str], age: int = None
    ) -> Dict[bool, Pets]:
        """Registry Use Case"""
        raise NotImplementedError("RegisterPet.registry() is not implemented")
