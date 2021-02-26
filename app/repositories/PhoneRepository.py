import psycopg2
from flask import jsonify
import database

dbconn = database.get_connection()


class Phone:

    @classmethod
    def get_all(cls):
        query = """SELECT * FROM phone_number"""
        cur = dbconn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        my_list = []
        for row in rows:
            my_list.append(row)
        return jsonify(my_list)

    @classmethod
    def get_phone_by_id(cls, user_id):
        query = """SELECT * FROM phone_number WHERE user_id = %s"""
        cur = dbconn.cursor()
        cur.execute(query, (user_id,))
        rows = cur.fetchall()
        my_list = []
        for row in rows:
            my_list.append(row)
        return my_list

    @classmethod
    def create_phone(cls, data):
        query = """ INSERT INTO phone_number (user_id, number_type, number) VALUES (%s,%s,%s)"""
        record_to_insert = (data['user_id'], data['number_type'], data['number'])
        cur = dbconn.cursor()
        cur.execute(query, record_to_insert)
        dbconn.commit()
        cur.close()

    @classmethod
    def update_phone(cls, data):
        query = """ Update phone_number set number_type = %s, number = %s  where user_id = %s"""
        record_to_insert = (data['number_type'], data['number'], data['user_id'])
        cur = dbconn.cursor()
        cur.execute(query, record_to_insert)
        dbconn.commit()
        cur.close()

    @classmethod
    def delete_phone(cls, data):
        query = """ Delete from phone_number where user_id = %s"""
        cur = dbconn.cursor()
        cur.execute(query, (data,))
        dbconn.commit()
        cur.close()
