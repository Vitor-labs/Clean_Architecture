from abc import ABC, abstractmethod
from typing import List

from src.domain.models import Users


class UserRepositoryInterface(ABC):
    """Interface to Pet Repository"""

    @abstractmethod
    def insert_user(
        self, id: int, name: str, specie: str, age: int, user_id: int
    ) -> Users:
        """Abstract Method"""
        raise Exception("Method not implemented")

    @abstractmethod
    def select_user(self, id: int = None, user_id: int = None) -> List[Users]:
        """Abstract Method"""
        raise Exception("Method not implemented")
