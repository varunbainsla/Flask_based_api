from flask import Flask, request, jsonify
from usecase.users.add_template import AddTemplateUsecase
from usecase.users.delete_template import DeleteTemplateUsecase
from usecase.users.get_all_template import GetAllTemplateUsecase
from usecase.users.get_template import GetTemplateUsecase
from usecase.users.update_template import UpdateTemplateUsecase
from usecase.users.user_signup import user_signup_usecase
from utils.authentication import authenticate_user
from utils.authorization import jwtBearer
from utils.error_handler import CustomErrorHandler

app = Flask(__name__)
app.wsgi_app = jwtBearer(app.wsgi_app)

# Routes

# User Registration
@app.route('/register', methods=['POST'])
def register():
    data =user_signup_usecase()
    return jsonify(data)

# User Login
@app.route('/login', methods=['POST'])
def login():
    data= authenticate_user()
    return jsonify(data)

# Add new template / Get all template
@app.route('/template',methods=['POST','GET'])
def add_template():
    if request.method == 'POST':
        data=AddTemplateUsecase()
    elif request.method == 'GET':
         data=GetAllTemplateUsecase()
    return jsonify(data)


# Get/Delete/Update Specific Template
@app.route('/template/',methods=['GET','POST','PUT','DELETE'])
def template():
    if request.method == 'GET':
        data=GetTemplateUsecase()

    elif request.method == 'PUT':
        data = UpdateTemplateUsecase()

    elif request.method == 'DELETE':

        data = DeleteTemplateUsecase()
    return jsonify(data)

# Error handler for the custom exception
@app.errorhandler(CustomErrorHandler)
def handle_custom_exception(error):
    response = jsonify({'message': error.description})
    response.status_code = error.code
    return response

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
