import psycopg2
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
        my_list = []
        for row in rows:
            my_list.append(row)
        return jsonify(my_list)

    @classmethod
    def get_user_by_id(cls, id):
        query = """SELECT * FROM users WHERE id = %s"""
        cur = dbconn.cursor()
        cur.execute(query, (id,))
        rows = cur.fetchall()
        my_list = []
        for row in rows:
            my_list.append(row)
        return my_list

    @classmethod
    def create_user(cls, data):
        query = """ INSERT INTO users (full_name, birthdate, address, gender) VALUES (%s,%s,%s,%s)"""
        record_to_insert = (data['full_name'], data['birthdate'], data['address'], data['gender'])
        cur = dbconn.cursor()
        cur.execute(query, record_to_insert)
        dbconn.commit()
        cur.close()

    @classmethod
    def update_user(cls, data):
        query = """ Update users set full_name = %s, birthdate = %s, address = %s ,gender = %s  where id = %s"""
        record_to_insert = (data['full_name'], data['birthdate'], data['address'], data['gender'], data['id'])
        cur = dbconn.cursor()
        cur.execute(query, record_to_insert)
        dbconn.commit()
        cur.close()

    @classmethod
    def delete_user(cls, data):
        query = """ Delete from users where id = %s"""
        cur = dbconn.cursor()
        cur.execute(query, (data,))
        dbconn.commit()
        cur.close()
