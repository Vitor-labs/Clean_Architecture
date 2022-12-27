from faker import Faker

from .find import FindPet
from src.infra.test import PetRepositorySpy

faker = Faker()


def test_find_by_id_success():
    """Testing Case: find Pet by id Succeds"""
    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attrs = {
        "id": faker.random_number(digits=2),
        "user_id": faker.random_number(digits=2),
    }

    response = find_pet.by_id(id=attrs["id"])

    assert pet_repo.select_pet_params["id"] == attrs["id"]

    assert response["Success"] is True
    assert response["Data"]


def test_find_by_id_fail():
    """Testing Case: find Pet by id Fails"""
    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attrs = {"id": faker.random_number(digits=2), "user_id": faker.name()}

    response = find_pet.by_id(id=attrs["user_id"])

    assert pet_repo.select_pet_params == {}

    assert response["Success"] is False
    assert response["Data"] is None


def test_find_by_user_id_success():
    """Testing Case: find Pet by the user id Succeds"""
    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attrs = {
        "id": faker.random_number(digits=2),
        "user_id": faker.random_number(digits=2),
    }

    response = find_pet.by_user_id(user_id=attrs["user_id"])

    assert pet_repo.select_pet_params["user_id"] == attrs["user_id"]

    assert response["Success"] is True
    assert response["Data"]


def test_find_by_user_id_fail():
    """Testing Case: find Pet by the user id Fails"""
    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attrs = {"id": faker.random_number(digits=2), "user_id": faker.name()}

    response = find_pet.by_id(id=attrs["user_id"])

    assert pet_repo.select_pet_params == {}

    assert response["Success"] is False
    assert response["Data"] is None


def test_find_by_id_and_user_id_success():
    """Testing Case: find Pet by the user id Succeds"""
    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attrs = {
        "id": faker.random_number(digits=2),
        "user_id": faker.random_number(digits=2),
    }

    response = find_pet.by_id_and_user_id(id=attrs["id"], user_id=attrs["user_id"])

    assert pet_repo.select_pet_params["id"] == attrs["id"]

    assert response["Success"] is True
    assert response["Data"]


def test_find_by_id_and_user_id_fail():
    """Testing Case: find Pet by the user id Fails"""
    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attrs = {"id": faker.random_number(digits=2), "user_id": faker.name()}

    response = find_pet.by_id_and_user_id(id=attrs["user_id"], user_id=attrs["user_id"])

    assert pet_repo.select_pet_params == {}

    assert response["Success"] is False
    assert response["Data"] is None
