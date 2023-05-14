from typing import Type

from src.presenters.errors.http_errors import HTTPErrors
from src.presenters.helpers.http_models import HTTPRequest, HTTPResponse
from ...domain.use_cases import FindUser


class FindUserController:
    """Class to define a controller to find_user use case"""
    def __init__(self, find_user_use_case: Type[FindUser]) -> None:
        self.find_user_use_case = find_user_use_case

    def handle(self, http_request: Type[HTTPRequest]) -> HTTPResponse:
        """Calls find_user use case

        Args:
            http_request (Type[HTTPRequest]): request

        Returns:
            HTTPResponse: response
        """
        response = None

        if not http_request.query:
            error = HTTPErrors.error_400()
            return HTTPResponse(
                status_code=error["status_code"],
                body=error["body"]
            )

        query_string_params = http_request.query.keys()

        if "id" in query_string_params and "name" in query_string_params:
            user_id = http_request.query["id"]
            user_name = http_request.query["name"]

            response = self.find_user_use_case.by_id_and_name(
                id = user_id,
                name = user_name
            )

        elif "id" in query_string_params and "name" not in query_string_params:
            user_id = http_request.query["id"]

            response = self.find_user_use_case.by_id(
                id = user_id,
            )

        elif "id" not in query_string_params and "name" in query_string_params:
            user_name = http_request.query["name"]

            response = self.find_user_use_case.by_name(
                name = user_name
            )

        else:
            response = {"Success": False, "Data": None}

        if response["Success"] is False:
            error = HTTPErrors.error_422()
            return HTTPResponse(
                status_code=error["status_code"],
                body = error["body"]
            )
    
        return HTTPResponse(
            status_code=200,
            body=response["Data"]
        )
