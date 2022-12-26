from faker import Faker

from .register import RegisterUser
from src.infra.test import UserRepositorySpy

faker = Faker()


def test_register_success():
    """Test for the success case of registry method"""
    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    attributes = {"name": faker.name(), "password": faker.password()}

    response = register_user.register(
        name=attributes["name"], password=attributes["password"]
    )

    assert user_repo.insert_user_params["name"] == attributes["name"]
    assert user_repo.insert_user_params["password"] == attributes["password"]

    assert response["Success"] is True
    assert response["Data"]


def test_register_fail():
    """Test for the fail case of registry method"""
    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    attributes = {"name": faker.random_number(), "password": faker.password()}

    response = register_user.register(
        name=attributes["name"], password=attributes["password"]
    )

    assert user_repo.insert_user_params == {}

    assert response["Success"] is False
    assert response["Data"] is None
