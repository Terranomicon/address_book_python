from datetime import datetime

from flask import jsonify
import time
from repositories.UserRepository import User

from .Controller import Controller as Con
from Logger import logger


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

        if not is_date_valid(data.get('birthdate')):
            return Con.response({'error': 'Birthdate not valid'}, 400)

        if data.get('address') == '' or data.get('address') is None:
            return Con.response({'error': 'Address required'}, 400)

        if data.get('gender') == '' or data.get('gender') is None:
            return Con.response({'error': 'Gender required'}, 400)

        try:
            User.create_user(data)
            logger.info('create object %s', data)
            return Con.response({'OK': '200'}, 200)
        except Exception as error:
            logger.error('error creating %s', error)
            return Con.response({'Error': '500'}, 500)

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
            if data.get('birthdate') == '':
                return Con.response({'error': 'Invalid parameters. Birthdate must not be empty'}, 400)

            if not is_date_valid(data.get('birthdate')):
                return Con.response({'error': 'Birthdate not valid'}, 400)
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
        try:
            User.update_user(new_user_data)
            logger.info('update object with new data %s', new_user_data)
            return Con.response({'OK': '200'}, 200)
        except Exception as error:
            logger.error('error updating %s', error)
            return Con.response({'Error': '500'}, 500)

    @classmethod
    def delete_user(cls, data):
        if data.get('id') == '' or data.get('id') is None:
            return Con.response({'error': 'Invalid parameters. Id required'}, 400)

        user = User.get_user_by_id(data.get('id'))
        if not user:
            return Con.response({'error': 'User not found'}, 400)
        try:
            User.delete_user(data.get('id'))
            return Con.response({'OK': '200'}, 200)
        except Exception as error:
            logger.error('error delete %s', error)
            return Con.response({'Error': '500'}, 500)


def is_date_valid(date_text):
    try:
        if date_text != datetime.strptime(date_text, "%Y-%m-%d").strftime('%Y-%m-%d'):
            raise ValueError
        return True
    except ValueError:
        return False
