from typing import Type

from ...presenters.helpers.http_models import HTTPRequest, HTTPResponse
from ...presenters.errors import HTTPErrors
from ...domain.use_cases.register_pet import RegisterPet

class RegisterPetController:
    """Class to define the Route for use case register pet"""
    def __init__(self, register_pet_use_case: Type[RegisterPet]) -> None:
        self.register_pet_use_case = register_pet_use_case

    def route(self, http_request: Type[HTTPRequest]) -> HTTPResponse:
        """Calls register pet use case

        Args:
            http_request (Type[HTTPRequest]): Web Request for use case activation

        Returns:
            HTTPResponse: Response for use case calling
        """
        response = None

        if not http_request.body:
            error = HTTPErrors.error_400()
            return HTTPResponse(
                        status_code = error["status_code"],
                                body = error["body"]
                    )

        body_params = http_request.body.keys()

        if "name" in body_params and "species" in body_params and "user" in body_params:
            user_info = http_request.body["user"].keys()

            if "user_id" in user_info or "name" in user_info:
                name = http_request.body["name"]
                specie = http_request.body["specie"]
                user = http_request.body["user"]
                age = None

                if "age" in body_params:
                    age = http_request.body["age"]
                
                response = self.register_pet_use_case.registry(name, specie, user, age)

            else:
                response = {"Success": False, "Data": None}

        else:
            response = {"Success": False, "Data": None}

        if response["Success"] is False:
            error = HTTPErrors.error_422()
            return HTTPResponse(
                status_code = error["status_code"],
                body = error["body"]
            )
        return HTTPResponse(status_code=200, body=response["Data"])
    