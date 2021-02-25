from flask import Flask
import controllers.UserController

app = Flask(__name__)


@app.route('/users', methods=['POST'])
def get_users():
    controllers.UserController.UserController.get_users()


# @app.route('/users/<id>', methods=['POST'])
# def get_user_by_id(id: int):
#     UserController.get_user_by_id(id)


# @app.route('/users', methods=['PUT'])
# def create_user(full_name: str):
#     UserController.create_user(full_name)
#
#
# @app.route('/users', methods=['PATCH'])
# def create_user(full_name: str):
#     UserController.update_user(full_name)
#
#
# @app.route('/users', methods=['DELETE'])
# def create_user(full_name: str):
#     UserController.create_user(full_name)


if __name__ == '__main__':
    app.run()
