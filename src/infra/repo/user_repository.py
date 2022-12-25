# pylint: disable=E1101
from typing import List

from src.data.interfaces import UserRepositoryInterface
from src.domain.models import Users
from src.infra.config import DBConnectionManager
from src.infra.entities import Users as UserModel


class UserRepository(UserRepositoryInterface):
    """Class that manages the User Repository"""

    @classmethod
    def insert_user(cls, name: str, password: str) -> Users:
        """Insert data in user entity
        :param - name: person name
               - password: user password
        :return - Named Tuple with new User
        """

        with DBConnectionManager() as conn:
            try:
                new_user = UserModel(name=name, password=password)
                conn.session.add(new_user)
                conn.session.commit()

                return Users(
                    id=new_user.id, name=new_user.name, password=new_user.password
                )
            except:
                conn.session.rollback()
                raise
            finally:
                conn.session.close()

        return None

    @classmethod
    def select_user(cls, id: int = None, username: str = None) -> List[Users]:
        """Select data in the user entity by id and/or name.
        :param - id: The id of the user
               - name: The name of the user
        :return: A list of users selecteds"""

        try:
            query = None

            if id and not username:
                with DBConnectionManager() as conn:
                    data = conn.session.query(UserModel).filter_by(id=id).one()
                    query = [data]

            elif not id and username:
                with DBConnectionManager() as conn:
                    data = conn.session.query(UserModel).filter_by(name=username).one()
                    query = [data]

            elif id and username:
                with DBConnectionManager() as conn:
                    data = (
                        conn.session.query(UserModel)
                        .filter_by(id=id, name=username)
                        .one()
                    )
                    query = [data]

            return query

        except:
            conn.session.rollback()
            raise
        finally:
            conn.session.close()
