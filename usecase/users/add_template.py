from flask import request
from pymongo import MongoClient

from config import DATABASE_USER, DATABASE_PASSWORD
from database.datastore import UserDataStore, TemplateDataStore
from entity.template import template_info


def AddTemplateUsecase():
    ''''
    Usecase for storing new template
    '''
    payload=template_info(
                template_name=request.json["template_name"],
                subject=request.json["subject"],
                body=request.json["body"]
        )
    with MongoClient(
        f"mongodb+srv://{DATABASE_USER}:{DATABASE_PASSWORD}@cluster0.4etijnx.mongodb.net/?retryWrites=true&w=majority"
    ) as client:
        repo = TemplateDataStore(client)

        try :
            data = repo.add_template(payload)
            return {
                "status":200,
                "message": "Template Added Successfully"
            }

        except:
            return {
                "status":403,
                "message": "Unable to store template! Internal Error"
            }
