from faker import Faker

from .find_user_controller import FindUserController
from ...data.test import FindUserSpy
from ...infra.test import UserRepositorySpy
from ..helpers import HTTPRequest


faker = Faker()
# Falta testar os parametros de query
def find_user_controller_success():
    """Testing Case: find user by id Succeds"""
    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)

    http_request = HTTPRequest(query={
        "id": faker.random_number(),
        "name": faker.name()
    })

    response = find_user_controller.handle(http_request)
    print(response)
    assert find_user_use_case.by_id_and_name_params["id"] == http_request.query["id"]
    assert find_user_use_case.by_id_and_name_params["name"] == http_request.query["name"]

    assert response.status_code == 200
    assert response.body

def find_user_controller_fail_422():
    """Testing Case: find user by id fails"""
    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)

    http_request = HTTPRequest(query={
        "id": faker.name(),
        "name": faker.ramdom_number()
    })

    response = find_user_controller.handle(http_request)

    assert not find_user_use_case.by_id_and_name_params

    assert response.status_code == 422
    assert "error" in response.body

def find_user_controller_fail_400():
    """Testing Case: find user by id fails"""
    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)

    http_request = HTTPRequest(query={
    })

    response = find_user_controller.handle(http_request)

    assert not find_user_use_case.by_id_and_name_params

    assert response.status_code == 400
    assert "error" in response.body
