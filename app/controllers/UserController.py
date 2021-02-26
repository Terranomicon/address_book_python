from flask import jsonify
from repositories.UserRepository import User

from .Controller import Controller as Con


class UserController:

    @classmethod
    def get_all_users(cls):
        return User.get_all()

    @classmethod
    def get_user_by_id(cls, id: int):
        if id == '':
            return Con.response({'error': 'id required'}, 400)
        else:
            return jsonify(User.get_user_by_id(id))

    @classmethod
    def create_user(cls, data):
        if data.get('full_name') == '' or data.get('full_name') is None:
            return Con.response({'error': 'Full name required'}, 400)

        if data.get('birthdate') == '' or data.get('birthdate') is None:
            return Con.response({'error': 'Birthdate required'}, 400)

        # if not valid_date(data.get('birthdate')): #сделать
        #     return Con.response({'error': 'Incorrect date'}, 400)
        # test = get_date(data.get('birthdate'))

        if data.get('address') == '' or data.get('address') is None:
            return Con.response({'error': 'Address required'}, 400)

        if data.get('gender') == '' or data.get('gender') is None:
            return Con.response({'error': 'Gender required'}, 400)
        User.create_user(data)
        return Con.response({'OK': '200'}, 200)

    @classmethod
    def update_user(cls, data):
        new_user_data = {}
        if data.get('id') == '' or data.get('id') is None:
            return Con.response({'error': 'Invalid parameters. Id required'}, 400)

        user = User.get_user_by_id(data.get('id'))
        if not user:
            return Con.response({'error': 'User not found'}, 400)
        else:
            new_user_data['id'] = data.get('id')

        if data.get('full_name') is not None:
            if data.get('full_name') == '':
                return Con.response({'error': 'Invalid parameters. Name must not be empty'}, 400)
            else:
                new_user_data['full_name'] = data.get('full_name')
        else:
            new_user_data['full_name'] = user[0][0]

        if data.get('birthdate') is not None:
            if data.get('birthdate') == '':  # добавить валидацию даты
                return Con.response({'error': 'Invalid parameters. Birthdate must not be empty'}, 400)
            else:
                new_user_data['birthdate'] = data.get('birthdate')
        else:
            new_user_data['birthdate'] = user[0][1]

        if data.get('address') is not None:
            if data.get('address') == '':
                return Con.response({'error': 'Invalid parameters. Address must not be empty'}, 400)
            else:
                new_user_data['address'] = data.get('address')
        else:
            new_user_data['address'] = user[0][2]

        if data.get('gender') is not None:
            if data.get('gender') == '':
                return Con.response({'error': 'Invalid parameters. Gender must not be empty'}, 400)
            else:
                new_user_data['gender'] = data.get('gender')
        else:
            new_user_data['gender'] = user[0][3]

        User.update_user(new_user_data)
        return Con.response({'OK': '200'}, 200)

    @classmethod
    def delete_user(cls, data):
        if data.get('id') == '' or data.get('id') is None:
            return Con.response({'error': 'Invalid parameters. Id required'}, 400)

        user = User.get_user_by_id(data.get('id'))
        if not user:
            return Con.response({'error': 'User not found'}, 400)

        User.delete_user(data.get('id'))
        return Con.response({'OK': '200'}, 200)
