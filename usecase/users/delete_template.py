from flask import request
from pymongo import MongoClient

from config import DATABASE_USER, DATABASE_PASSWORD
from database.datastore import  TemplateDataStore


def DeleteTemplateUsecase():
    '''
    Usecase for deleting specific template
    '''
    template_id=request.args.get("template_id")
    with MongoClient(
        f"mongodb+srv://{DATABASE_USER}:{DATABASE_PASSWORD}@cluster0.4etijnx.mongodb.net/?retryWrites=true&w=majority"
    ) as client:
        repo = TemplateDataStore(client)

        try :
            repo.delete_template(template_id=template_id)
            return {
                "status":200,
                "message": "Template Deleted Successfully"
            }

        except:
            return {
                "status":403,
                "message": "Unable to Delete template! Internal Error"
            }
