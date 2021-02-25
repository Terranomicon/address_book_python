# from app.repositories.Repository import Repository
# from app import database
from flask import jsonify
import database

dbconn = database.get_connection()


class User:

    @classmethod
    def get_all(cls):
        query = """SELECT * FROM users"""
        cur = dbconn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        response = ''
        my_list = []
        for row in rows:
            my_list.append(row)
        return jsonify(my_list)

    @classmethod
    def get_user_by_id(cls, id):
        query = """SELECT * FROM users WHERE id = """ + id
        cur = dbconn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        response = ''
        my_list = []
        for row in rows:
            my_list.append(row)
        return jsonify(my_list)
#
# @classmethod
#     def create(full_name: str):
#         query = ""
#         pass
