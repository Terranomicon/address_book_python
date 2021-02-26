from flask import jsonify
from repositories.EmailRepository import Email

from .Controller import Controller as Con


class EmailController:

    @classmethod
    def get_all_emails(cls):
        return Email.get_all()

    @classmethod
    def get_email_by_id(cls, user_id: int):
        if user_id == '':
            return Con.response({'error': 'User id required'}, 400)
        else:
            return jsonify(Email.get_email_by_id(user_id))

    @classmethod
    def create_email(cls, data):
        if data.get('type') == '' or data.get('type') is None:
            return Con.response({'error': 'Email type required'}, 400)

        if data.get('type') not in ['Личный', 'Рабочий']:
            return Con.response({'error': 'Email type not allowed'}, 400)

        if data.get('email') == '' or data.get('email') is None:
            return Con.response({'error': 'Email required'}, 400)

        if data.get('user_id') == '' or data.get('user_id') is None:
            return Con.response({'error': 'Invalid parameters. User id required'}, 400)

        email = Email.get_email_by_id(data.get('user_id'))
        if email:
            return Con.response({'error': 'Email exist'}, 400)
        Email.create_email(data)
        return Con.response({'OK': '200'}, 200)

    @classmethod
    def update_email(cls, data):
        new_email_data = {}
        if data.get('user_id') == '' or data.get('user_id') is None:
            return Con.response({'error': 'Invalid parameters. User id required'}, 400)

        email = Email.get_email_by_id(data.get('user_id'))
        if not email:
            return Con.response({'error': 'Email not exist'}, 400)
        else:
            new_email_data['user_id'] = email[0][0]
        if data.get('type') is not None:
            if data.get('type') == '':
                return Con.response({'error': 'Invalid parameters. Number type must not be empty'}, 400)
            if data.get('type') not in ['Личный', 'Рабочий']:
                return Con.response({'error': 'Number type not allowed'}, 400)
            new_email_data['type'] = data.get('type')
        else:
            new_email_data['type'] = email[0][1]

        if data.get('email') is not None:
            if data.get('email') == '':  # добавить валидацию даты
                return Con.response({'error': 'Invalid parameters. Number must not be empty'}, 400)
            else:
                new_email_data['email'] = data.get('email')
        else:
            new_email_data['email'] = email[0][2]

        Email.update_email(new_email_data)
        return Con.response({'OK': '200'}, 200)

    @classmethod
    def delete_email(cls, data):
        if data.get('user_id') == '' or data.get('user_id') is None:
            return Con.response({'error': 'Invalid parameters. User id required'}, 400)

        email = Email.get_email_by_id(data.get('user_id'))
        if not email:
            return Con.response({'error': 'Email not found'}, 400)

        Email.delete_email(data.get('user_id'))
        return Con.response({'OK': '200'}, 200)
