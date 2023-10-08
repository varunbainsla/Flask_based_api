from datetime import datetime, timedelta

from flask import request
from jose import jwt
from pymongo import MongoClient

from config import JWT_SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, USER_DATABASE, DATABASE_USER, \
    DATABASE_PASSWORD
from database.datastore import UserDataStore
from utils.error_handler import  CustomErrorHandler
from utils.password_hasher import verify_password



def validate_jwt(token: str) -> str:
    try:
        decoded_jwt :dict = jwt.decode(token, JWT_SECRET_KEY, ALGORITHM)
        return decoded_jwt
    except:
        return None
def create_access_token(username: str, expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expires_delta,"sub":username}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)

    return encoded_jwt


def authenticate_user():
    '''
    Usecase to authenticate user
    :return: jwt token
    '''
    with MongoClient(
        f"mongodb+srv://{DATABASE_USER}:{DATABASE_PASSWORD}@cluster0.4etijnx.mongodb.net/?retryWrites=true&w=majority"
    ) as client:
        repo = UserDataStore(client)
        user =  repo.check_email_id(email_id=request.json["email"])
        if not user:
            raise CustomErrorHandler(
                status_code=403,
                detail="Incorrect username or password",
            )
        if not verify_password(request.json["password"], user['password']):
            raise CustomErrorHandler(
                status_code=403,
                detail="Incorrect username or password",
            )
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

        access_token = create_access_token(
            username= user['email'], expires_delta=access_token_expires
        )
    return {"access_token": access_token, "token_type": "bearer"}





