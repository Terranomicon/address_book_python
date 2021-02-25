from flask import Flask
from flask import request
import controllers.UserController

app = Flask(__name__)


@app.route('/users', methods=['POST'])
def get_users():
    if request.form:
        id = request.form['id']
        return controllers.UserController.UserController.get_user_by_id(id)
    else:
        return controllers.UserController.UserController.get_all_users()



# @app.route('/users', methods=['POST'])
# def get_user_by_id():
#     gg = request.form['id']
#     return controllers.UserController.UserController.get_user_by_id(gg)


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
