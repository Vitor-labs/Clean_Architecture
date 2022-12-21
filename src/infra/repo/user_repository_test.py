from faker import Faker

from .user_repository import UserRepository
from src.infra.config import DBConnectionManager

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
