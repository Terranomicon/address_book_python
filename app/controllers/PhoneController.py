from flask import jsonify
from repositories.PhoneRepository import Phone

from .Controller import Controller as Con
from Logger import logger


class PhoneController:

    @classmethod
    def get_all_phones(cls):
        return Phone.get_all()

    @classmethod
    def get_phone_by_id(cls, user_id: int):
        if user_id == '':
            return Con.response({'error': 'User id required'}, 400)
        else:
            return jsonify(Phone.get_phone_by_id(user_id))

    @classmethod
    def create_phone(cls, data):
        if data.get('number_type') == '' or data.get('number_type') is None:
            return Con.response({'error': 'Number type required'}, 400)

        if data.get('number_type') not in ['Городской', 'Мобильный']:
            return Con.response({'error': 'Number type not allowed'}, 400)

        if data.get('number') == '' or data.get('number') is None:
            return Con.response({'error': 'Number required'}, 400)

        if data.get('user_id') == '' or data.get('user_id') is None:
            return Con.response({'error': 'Invalid parameters. User id required'}, 400)

        phone = Phone.get_phone_by_id(data.get('user_id'))
        if phone:
            return Con.response({'error': 'Phone exist'}, 400)
        try:
            Phone.create_phone(data)
            logger.info('create object %s', data)
            return Con.response({'OK': '200'}, 200)
        except Exception as error:
            logger.error('error creating %s', error)
            return Con.response({'Error': '500'}, 500)

    @classmethod
    def update_phone(cls, data):
        new_phone_data = {}
        if data.get('user_id') == '' or data.get('user_id') is None:
            return Con.response({'error': 'Invalid parameters. User id required'}, 400)

        phone = Phone.get_phone_by_id(data.get('user_id'))
        if not phone:
            return Con.response({'error': 'Phone not exist'}, 400)
        else:
            new_phone_data['user_id'] = phone[0][0]
        if data.get('number_type') is not None:
            if data.get('number_type') == '':
                return Con.response({'error': 'Invalid parameters. Number type must not be empty'}, 400)
            if data.get('number_type') not in ['Городской', 'Мобильный']:
                return Con.response({'error': 'Number type not allowed'}, 400)
            new_phone_data['number_type'] = data.get('number_type')
        else:
            new_phone_data['number_type'] = phone[0][1]

        if data.get('number') is not None:
            if data.get('number') == '':
                return Con.response({'error': 'Invalid parameters. Number must not be empty'}, 400)
            else:
                new_phone_data['number'] = data.get('number')
        else:
            new_phone_data['number'] = phone[0][2]
        try:
            Phone.update_phone(new_phone_data)
            logger.info('update object with new data %s', new_phone_data)
            return Con.response({'OK': '200'}, 200)
        except Exception as error:
            logger.error('error updating %s', error)
            return Con.response({'Error': '500'}, 500)

    @classmethod
    def delete_phone(cls, data):
        if data.get('user_id') == '' or data.get('user_id') is None:
            return Con.response({'error': 'Invalid parameters. User id required'}, 400)

        phone = Phone.get_phone_by_id(data.get('user_id'))
        if not phone:
            return Con.response({'error': 'Phone not found'}, 400)
        try:
            Phone.delete_phone(data.get('user_id'))
            return Con.response({'OK': '200'}, 200)
        except Exception as error:
            logger.error('error delete %s', error)
            return Con.response({'Error': '500'}, 500)
