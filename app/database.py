import configparser

import psycopg2
from psycopg2 import OperationalError

config = configparser.ConfigParser()  # создаём объекта парсера
config.read("../config.ini")  # читаем конфиг


def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


connection = create_connection(config["database"]["dbname"], config["database"]["user"], config["database"]["password"],
                               config["database"]["host"], config["database"]["port"])


def get_connection():
    if not connection:
        create_connection(config["database"]["dbname"], config["database"]["user"], config["database"]["password"],
                          config["database"]["host"], config["database"]["port"])
    return connection
