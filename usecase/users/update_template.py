from flask import request
from pymongo import MongoClient

from config import DATABASE_USER, DATABASE_PASSWORD
from database.datastore import UserDataStore, TemplateDataStore
from entity.template import template_info


def UpdateTemplateUsecase():

    '''
    Usecase for updating specific template using :template_id
    '''

    template_id=request.args.get("template_id")
    payload=template_info(
                template_name=request.json["template_name"],
                subject=request.json["subject"],
                body=request.json["body"],
                template_id=template_id

        )
    print(payload)
    with MongoClient(
        f"mongodb+srv://{DATABASE_USER}:{DATABASE_PASSWORD}@cluster0.4etijnx.mongodb.net/?retryWrites=true&w=majority"
    ) as client:
        repo = TemplateDataStore(client)

        try :
            data = repo.update_template(payload)
            return {
                "status":200,
                "message": "Template Updated Successfully",
                "data" : data
            }

        except:
            return {
                "status":403,
                "message": "Unable to Update template! Internal Error"
            }
