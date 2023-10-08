from flask import request
from pymongo import MongoClient

from config import DATABASE_USER, DATABASE_PASSWORD
from database.datastore import UserDataStore, TemplateDataStore
from entity.template import template_info


def GetTemplateUsecase():
    '''
    Usecase for fetching specific template using :template_id
    '''
    template_id=request.args.get("template_id")
    with MongoClient(
        f"mongodb+srv://{DATABASE_USER}:{DATABASE_PASSWORD}@cluster0.4etijnx.mongodb.net/?retryWrites=true&w=majority"
    ) as client:
        repo = TemplateDataStore(client)

        try :
            data = repo.get_template(template_id)
            return {
                "status":200,
                "data" : data,
                "message": "Template Fetched Successfully"
            }

        except:
            return {
                "status":403,
                "message": "Unable to Fetch template! Internal Error"
            }
