# from app.repositories.Repository import Repository
from app import database

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
        return my_list
#
# @classmethod
#     def create(full_name: str):
#         query = ""
#         pass
