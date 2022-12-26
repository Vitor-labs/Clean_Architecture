from abc import ABC, abstractclassmethod
from typing import Dict

from src.domain.models import Users


class RegisterUser(ABC):
    """Interface to RegisterUser use case"""

    @abstractclassmethod
    def register(cls, name: str, password: str) -> Dict[bool, Users]:
        """Register use case"""
        raise NotImplementedError("Method not implemented: RegisterUser")
