from typing import Dict


class HTTPErrors:
    """Class to define error in protocol HTTP"""
    @staticmethod
    def error_422() -> Dict:
        """Unprocessable Entity"""
        return {"status_code": 422,
                "body":{
                    "error": "Unprocessable Entity"
                }
            }
    
    @staticmethod
    def error_400() -> Dict:
        """Bad Request"""
        return {"status_code": 400,
                "body":{
                    "error": "Bad Request"
                }
            }
