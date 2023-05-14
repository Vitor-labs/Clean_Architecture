from typing import Dict


class HTTPRequest:
    """Class to represent a HTTP Request"""
    def __init__(self, header: Dict = None, body: Dict = None, query: Dict = None):
        self.header = header
        self.body = body
        self.query = query

    def __repr__(self):
        return f'HTTPRequest(header={self.header},body={self.body},query={self.query})'
    
class HTTPResponse:
    """Class to represent a HTTP Response"""
    def __init__(self, status_code: int = None, body: Dict = None):
        self.status_code = status_code
        self.body = body

    def __repr__(self):
        return f'HTTPResponse(status_code={self.status_code},body={self.body})'   
