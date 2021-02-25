import json

from flask import Flask, Response, jsonify
from flask import request
import controllers.UserController

app = Flask(__name__)


@app.route('/users', methods=['POST'])
def get_users():
    if request.form:
        id = request.form['id']
        return jsonify(controllers.UserController.UserController.get_user_by_id(id))
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


if __name__ == '__main__':
    app.run()
