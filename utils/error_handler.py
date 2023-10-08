from werkzeug.exceptions import HTTPException
import typing


class CustomErrorHandler(HTTPException):

  def __init__(self,status_code,detail):
    self.code = status_code
    self.description = detail

