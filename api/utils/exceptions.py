
class APIException(Exception):
    status_code = 500
    message = "Generic Exception"

    def __init__(self, message=None, status_code=None):
        self.message = message
        self.status_code = status_code or self.status_code


class UnauthorizedException(APIException):
    status_code = 401
    message = "Unauthorized"