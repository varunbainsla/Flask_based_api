from flask import request
from pymongo import MongoClient

from config import DATABASE_USER, DATABASE_PASSWORD
from database.datastore import UserDataStore, TemplateDataStore
from entity.template import template_info


def GetAllTemplateUsecase():

    ''''
    Usecase for fetching all templates
    :return : List[template]
    '''

    with MongoClient(
        f"mongodb+srv://{DATABASE_USER}:{DATABASE_PASSWORD}@cluster0.4etijnx.mongodb.net/?retryWrites=true&w=majority"
    ) as client:
        repo = TemplateDataStore(client)

        try :
            data = repo.get_all_template()
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
