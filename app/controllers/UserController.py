# from Controller import Controller
# from flask import Response

# from app.repositories import UserRepository
# from app.repositories.UserRepository import User
from app.repositories.UserRepository import User


class UserController:

    @classmethod
    def get_users(cls):
        User.get_all()

    # @classmethod
    # def get_user_by_id(cls, id: int):
    #     pass
    #
    # @classmethod
    # def create_user(cls, full_name: str):
    #     pass
