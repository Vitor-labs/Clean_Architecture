from abc import ABCMeta, abstractmethod
from typing import Dict, List

from src.domain.models import Users


class FindUser(metaclass=ABCMeta):
    """Interface to FindUser use case"""

    @classmethod
    @abstractmethod
    def by_id(cls, id: int) -> Dict[bool, List[Users]]:
        """Case by ID"""
        raise NotImplementedError("FindUser.by_id() is not implemented")

    @classmethod
    @abstractmethod
    def by_name(cls, name: str) -> Dict[bool, List[Users]]:
        """Case by Name"""
        raise NotImplementedError("FindUser.by_name() is not implemented")

    @classmethod
    @abstractmethod
    def by_id_and_name(cls, id: int, name: str) -> Dict[bool, List[Users]]:
        """Case by ID and Name"""
        raise NotImplementedError("FindUser.by_id_and_name() is not implemented")
