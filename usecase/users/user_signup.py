from flask import request
from pymongo import MongoClient

from config import DATABASE_USER, DATABASE_PASSWORD
from database.datastore import UserDataStore
from entity.user import user_info

def user_signup_usecase():
    '''
    Usecase for new user registration
    '''
    payload=user_info(
                    first_name = request.json["first_name"],
                    last_name=request.json["last_name"],
                    email=request.json["email"],
                    password=request.json["password"],
    )
    print(payload)
    with MongoClient(
        f"mongodb+srv://{DATABASE_USER}:{DATABASE_PASSWORD}@cluster0.4etijnx.mongodb.net/?retryWrites=true&w=majority"
    ) as client:
        repo = UserDataStore(client)
        check = repo.check_email_id(email_id=payload.email)
        if not check :
            repo.create_user(payload)
            return {
                "status":200,
                "message": "User Created Successfull"
            }

        else:
            return {
                "status":403,
                "message": "User with same email id present"
            }
