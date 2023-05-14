from faker import Faker

from src.data.test import FindUserSpy
from src.infra.test import PetRepositorySpy, UserRepositorySpy
from .register import RegisterPet

faker = Faker()


def test_register_pet_success():
    """
    test for register per use case.
    should be a success.
    """

    pet_repo = PetRepositorySpy()
    find_user = FindUserSpy(UserRepositorySpy())
    register_pet = RegisterPet(pet_repo, find_user)

    attrs = {
        "name": faker.name(),
        "specie": faker.word(),
        "age": faker.random_number(digits=2),
        "user": {"id": faker.random_number(digits=2), "user_name": faker.name()},
    }
    response = register_pet.registry(
        name=attrs["name"], specie=attrs["specie"], age=attrs["age"], user=attrs["user"]
    )
    assert pet_repo.insert_pet_params["name"] == attrs["name"]
    assert pet_repo.insert_pet_params["specie"] == attrs["specie"]
    assert pet_repo.insert_pet_params["age"] == attrs["age"]

    assert find_user.by_id_and_name_params.get("id") == attrs.get("id")
    assert find_user.by_id_and_name_params.get("name") == attrs.get("user_name")

    assert response["Success"] is True
    assert response["Data"]
