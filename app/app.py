from flask import Flask
from flask import request
import controllers.UserController
import controllers.PhoneController
import controllers.EmailController

# import controllers.UserController

app = Flask(__name__)


@app.route('/users', methods=['POST'])
def get_users():
    if request.form:
        id = request.form['id']
        return controllers.UserController.UserController.get_user_by_id(id)
    else:
        return controllers.UserController.UserController.get_all_users()


@app.route('/users', methods=['PUT'])
def create_user():
    data = request.args
    return controllers.UserController.UserController.create_user(data)


@app.route('/users', methods=['PATCH'])
def update_user():
    data = request.args
    return controllers.UserController.UserController.update_user(data)


@app.route('/users', methods=['DELETE'])
def delete_user():
    data = request.args
    return controllers.UserController.UserController.delete_user(data)


@app.route('/phone', methods=['POST'])
def get_phones():
    if request.form:
        user_id = request.form['user_id']
        return controllers.PhoneController.PhoneController.get_phone_by_id(user_id)
    else:
        return controllers.PhoneController.PhoneController.get_all_phones()


@app.route('/phone', methods=['PUT'])
def create_phone():
    data = request.args
    return controllers.PhoneController.PhoneController.create_phone(data)


@app.route('/phone', methods=['PATCH'])
def update_phone():
    data = request.args
    return controllers.PhoneController.PhoneController.update_phone(data)


@app.route('/phone', methods=['DELETE'])
def delete_phone():
    data = request.args
    return controllers.PhoneController.PhoneController.delete_phone(data)


@app.route('/email', methods=['POST'])
def get_emails():
    if request.form:
        user_id = request.form['user_id']
        return controllers.EmailController.EmailController.get_email_by_id(user_id)
    else:
        return controllers.EmailController.EmailController.get_all_emails()


@app.route('/email', methods=['PUT'])
def create_email():
    data = request.args
    return controllers.EmailController.EmailController.create_email(data)


@app.route('/email', methods=['PATCH'])
def update_email():
    data = request.args
    return controllers.EmailController.EmailController.update_email(data)


@app.route('/email', methods=['DELETE'])
def delete_email():
    data = request.args
    return controllers.EmailController.EmailController.delete_email(data)


if __name__ == '__main__':
    app.run()
