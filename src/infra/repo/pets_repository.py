# pylint: disable=E1101
from typing import List

from src.data.interfaces import PetRepositoryInterface
from src.domain.models import Pets
from src.infra.entities import Pets as PetsModel
from src.infra.config import DBConnectionManager


class PetRepository(PetRepositoryInterface):
    """Class to manage Pet Repository"""

    @classmethod
    def insert_pet(cls, name: str, age: int, specie: str, user_id: int) -> Pets:
        """
        Insert data in Pet Entity
        :param - name: name of the new pet
               - age: age of the new pet
               - specie: Enum with species acepted
               - user_id: foreing key of the owner
        :return - named tuple with the new pet
        """
        with DBConnectionManager() as conn:
            try:
                new_pet = PetsModel(name=name, age=age, specie=specie, user_id=user_id)
                conn.session.add(new_pet)
                conn.session.commit()

                return Pets(
                    id=new_pet.id,
                    name=new_pet.name,
                    specie=new_pet.specie.value,
                    age=new_pet.age,
                    user_id=new_pet.user_id,
                )
            except:
                conn.session.rollback()
                raise
            finally:
                conn.session.close()

    @classmethod
    def select_pet(cls, id: int = None, user_id: int = None) -> List[Pets]:
        """Select data in the pet entity.
        :param - id: The id of the pet
               - name: The name of the pet
               - specie: species of pets
               - user_id: The id of the owner of the pet
        :return: A list of pets selected"""

        try:
            query = None

            if id and not user_id:
                with DBConnectionManager() as conn:
                    data = conn.session.query(PetsModel).filter_by(id=id).one()
                    query = data
            elif not id and user_id:
                with DBConnectionManager() as conn:
                    data = (
                        conn.session.query(PetsModel).filter_by(user_id=user_id).all()
                    )
                    query = data
            elif id and user_id:
                with DBConnectionManager() as conn:
                    data = (
                        conn.session.query(PetsModel)
                        .filter_by(id=id, user_id=user_id)
                        .one()
                    )
                    query = [data]

            return query
        except:
            conn.session.rollback()
            raise
        finally:
            conn.session.close()
