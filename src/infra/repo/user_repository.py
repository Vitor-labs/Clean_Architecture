# pylint: disable=E1101
from collections import namedtuple

from src.infra.config import DBConnectionManager
from src.infra.entities import Users


class UserRepository:
    """Class that manages the User Repository"""

    def insert_user(self, name: str, password: str) -> Users:
        """Insert data in user entity
        :param - name: person name
               - password: user password
        :return - Named Tuple with new User
        """
        data = namedtuple("Users", "id name, password")

        with DBConnectionManager() as conn:
            try:
                new_user = Users(name=name, password=password)
                conn.session.add(new_user)
                conn.session.commit()

                return data(
                    id=new_user.id, name=new_user.name, password=new_user.password
                )
            except:
                conn.session.rollback()
                raise
            finally:
                conn.session.close()
