import psycopg2
from flask import jsonify
import database

dbconn = database.get_connection()


class Email:

    @classmethod
    def get_all(cls):
        query = """SELECT * FROM email"""
        cur = dbconn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        my_list = []
        for row in rows:
            my_list.append(row)
        return jsonify(my_list)

    @classmethod
    def get_email_by_id(cls, user_id):
        query = """SELECT * FROM email WHERE user_id = %s"""
        cur = dbconn.cursor()
        cur.execute(query, (user_id,))
        rows = cur.fetchall()
        my_list = []
        for row in rows:
            my_list.append(row)
        return my_list

    @classmethod
    def create_email(cls, data):
        try:
            query = """ INSERT INTO email (user_id, type , email) VALUES (%s,%s,%s)"""
            record_to_insert = (data['user_id'], data['type'], data['email'])
            cur = dbconn.cursor()
            cur.execute(query, record_to_insert)
            dbconn.commit()
            cur.close()
        except psycopg2.Error as error:
            pass  # логи

    @classmethod
    def update_email(cls, data):
        try:
            query = """ Update email set type = %s, email = %s  where user_id = %s"""
            record_to_insert = (data['type'], data['email'], data['user_id'])
            cur = dbconn.cursor()
            cur.execute(query, record_to_insert)
            dbconn.commit()
            cur.close()
        except psycopg2.Error as error:
            print("Error in update operation", error)  # логи

    @classmethod
    def delete_email(cls, data):
        try:
            query = """ Delete from email where user_id = %s"""
            cur = dbconn.cursor()
            cur.execute(query, (data,))
            dbconn.commit()
            cur.close()
        except psycopg2.Error as error:
            print("Error in update operation", error)  # логи
