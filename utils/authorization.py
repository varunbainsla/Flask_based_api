from flask import Request, Response
from utils.authentication import  validate_jwt

from typing import Optional, Tuple


def get_authorization_scheme_param(
    authorization_header_value: Optional[str],
) -> Tuple[str, str]:
    if not authorization_header_value:
        return "", ""
    scheme, _, param = authorization_header_value.partition(" ")
    return scheme, param


class jwtBearer():
    def __init__(self,app,auto_Error : bool = True):
        self.auto_error = auto_Error
        self.app = app

    def __call__(self, environ, start_response):
        request = Request(environ)
        print("request",request)
        if request.path in ['/template','/template/']:
            authorization = request.headers.get("Authorization")
            scheme, credentials = get_authorization_scheme_param(authorization)

            if scheme.lower() != "bearer":
                    if self.auto_error:
                        res = Response("Invalid authentication credentials", mimetype='text/plain', status=401)
                        return res(environ, start_response)
            if not self.verify_jwt(credentials):
                            res = Response("Invalid authentication credentials", mimetype='text/plain', status=401)
                            return res(environ, start_response)
            else:
                return self.app(environ, start_response)
        else:
            return self.app(environ, start_response)



    def verify_jwt(self,jwt_token:str):
        isTokenValid : bool = False
        payload=validate_jwt(jwt_token)
        if payload:
            isTokenValid=True
        return  isTokenValid



