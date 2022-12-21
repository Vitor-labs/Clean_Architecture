from faker import Faker

from .user_repository import UserRepository
from src.infra.config import DBConnectionManager
from src.infra.entities import Users as UserModel

faker = Faker()
conn = DBConnectionManager()
user_repo = UserRepository()


def test_insert_user():
    """Should insert a new user"""

    name = faker.name()
    password = faker.password()

    engine = conn.get_engine()
    data = user_repo.insert_user(name, password)

    query_user = engine.execute(
        "SELECT * FROM users WHERE id={}".format(data.id)
    ).fetchone()
    engine.execute("DELETE from users WHERE id={}".format(data.id))

    assert query_user.id == data.id
    assert query_user.name == data.name
    assert query_user.password == data.password


def test_select_user():
    """Should select and compare a user in database"""

    user_id = faker.random_number(digits=5)
    name = faker.name()
    password = faker.password()

    data = UserModel(id=user_id, name=name, password=password)
    engine = conn.get_engine()

    engine.execute(
        "INSERT INTO users (id, name, password) VALUES ('{}', '{}', '{}')".format(
            user_id, name, password
        )
    )

    query1 = user_repo.select_user(id=user_id, username=name)
    query2 = user_repo.select_user(username=name)
    query3 = user_repo.select_user(id=user_id)

    assert data in query1
    assert data in query2
    assert data in query3

    engine.execute("DELETE FROM users WHERE id={}".format(user_id))
