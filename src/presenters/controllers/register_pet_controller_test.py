from faker import Faker

from src.data.test import RegisterPetSpy
from src.presenters.helpers import HTTPRequest
from src.infra.test import PetRepositorySpy, UserRepositorySpy

from .register_pet_controller import RegisterPetController


faker = Faker()

def test_route():
    """Test for route method in RegisterUserRoute"""
    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), UserRepositorySpy())
    register_pet_route = RegisterPetController(register_pet_use_case)

    attrs = {
        "name": faker.name(),
        "specie": "CAT",
        "age": faker.random_number(),
        "user": {
            "id": faker.random_number(),
            "name": faker.name()
        }
    }

    response = register_pet_route.route(HTTPRequest(body=attrs))

    # Testing input entry
    assert register_pet_use_case.registry_params["name"] == attrs["name"]
    assert register_pet_use_case.registry_params["specie"] == attrs["specie"]
    assert register_pet_use_case.registry_params["age"] == attrs["age"]
    assert register_pet_use_case.registry_params["user"] == attrs["user"]

    # Testing output response
    assert response.status_code == 200
    assert "error" not in response.body
