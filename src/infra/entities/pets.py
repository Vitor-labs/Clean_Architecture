from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from src.infra.config import Base
import enum


class PetsTypes(enum.Enum):
    """Definitions of Pets Types"""

    DOG = "DOG"
    CAT = "CAT"
    FISH = "FISH"
    HABBIT = "HABBIT"
    TURTLE = "TURTLE"


class Pets(Base):
    """Pets Entity"""

    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    specie = Column(Enum(PetsTypes), nullable=False)
    age = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return f"Pet: [name={self.name}, specie={self.specie}, user={self.user.id}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.name == other.name
            and self.specie == other.specie
            and self.age == other.age
            and self.user_id == other.user_id
        ):

            return True
        return False
