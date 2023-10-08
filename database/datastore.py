from config import DATABASE_NAME, TABLE_NAME, TEMPLATE_TABLE_NAME
from entity.template import template_info
from entity.user import user_info
from utils.password_hasher import get_hashed_password
from pymongo import errors


class UserDataStore:

    def __init__(self,client):

        self.database=client[f"{DATABASE_NAME}"]
        self.collection = self.database[f"{TABLE_NAME}"]



    def create_user(self,payload :user_info):
        json_data=payload.to_json()
        json_data["password"]=get_hashed_password(json_data["password"])

        try:
            self.collection.insert_one(json_data)
        except errors as e:
            print(f"Mongodb error: {e}")



    def check_email_id(self,email_id):
        try:
            query = { "email": f"{email_id.lower()}" }
            # Fetch all rows from the result set
            rows =  list(self.collection.find(query))
            if rows:
                return rows[0]

            else:
                 return False

        except errors.PyMongoError as e:
            print(f"Mongodb error: {e}")



class TemplateDataStore:
    def __init__(self,client):

        self.database=client[f"{DATABASE_NAME}"]
        self.collection = self.database[f"{TEMPLATE_TABLE_NAME}"]

    def validate_data(self,data):
        result=[]
        for item in data:
            del item['_id']
            result.append(item)
        return result

    def add_template(self,payload :template_info):
        json_data=payload.to_json()

        try:
            self.collection.insert_one(json_data)
            return json_data
        except errors as e:
            print(f"Mongodb error: {e}")

    def get_all_template(self):
        try:
            data = list(self.collection.find())
            return self.validate_data(data)
        except errors as e:
            print(f"Mongodb error: {e}")

    def get_template(self,template_id):
        try:
            query = { "template_id": f"{template_id}"}
            data = list(self.collection.find(query))
            return self.validate_data(data)
        except errors as e:
            print(f"Mongodb error: {e}")

    def update_template(self,payload):
        json_data=payload.to_json()
        query = { "template_id": f"{json_data['template_id']}" }
        newvalues = { "$set": json_data }

        try:
            self.collection.update_one(query, newvalues)
            return json_data
        except errors as e:
            print(f"Mongodb error: {e}")

    def delete_template(self,template_id):
        query = { "template_id": f"{template_id}" }
        try:
            self.collection.delete_one(query)

        except errors as e:
            print(f"Mongodb error: {e}")
