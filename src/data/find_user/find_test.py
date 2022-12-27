from faker import Faker

from .find import FindUser
from src.infra.test import UserRepositorySpy

faker = Faker()


def test_find_by_id_success():
    """Testing find user by id"""
    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {"id": faker.random_number(digits=2), "name": faker.name()}

    response = find_user.by_id(id=attributes["id"])

    assert user_repo.select_user_params["id"] == attributes["id"]

    assert response["Success"] is True
    assert response["Data"]


def test_find_by_id_fail():
    """Testing find user by id"""
    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {"id": faker.name(), "name": faker.name()}

    response = find_user.by_id(id=attributes["id"])

    assert user_repo.select_user_params == {}

    assert response["Success"] is False
    assert response["Data"] is None


def test_find_by_name_success():
    """Testing find user by Name"""
    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {"id": faker.random_number(digits=2), "name": faker.name()}

    response = find_user.by_name(name=attributes["name"])

    assert user_repo.select_user_params["name"] == attributes["name"]

    assert response["Success"] is True
    assert response["Data"]


def test_find_by_name_fail():
    """Testing find user by id"""
    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {
        "id": faker.name(),
        "name": faker.random_number(digits=2),
    }

    response = find_user.by_name(name=attributes["name"])

    assert user_repo.select_user_params == {}

    assert response["Success"] is False
    assert response["Data"] is None


def test_find_by_id_and_name_success():
    """Testing find user by id and Name"""
    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {"id": faker.random_number(digits=2), "name": faker.name()}

    response = find_user.by_id_and_name(id=attributes["id"], name=attributes["name"])

    assert user_repo.select_user_params["id"] == attributes["id"]
    assert user_repo.select_user_params["name"] == attributes["name"]

    assert response["Success"] is True
    assert response["Data"]


def test_find_by_id_and_name_fail():
    """Testing find user by id and Name"""
    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {"id": faker.name(), "name": faker.random_number(digits=2)}

    response = find_user.by_id_and_name(id=attributes["id"], name=attributes["name"])

    assert user_repo.select_user_params == {}

    assert response["Success"] is False
    assert response["Data"] is None
