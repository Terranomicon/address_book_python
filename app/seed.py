import random

import database
from faker import Faker

dbconn = database.get_connection()
fake = Faker('ru_RU')

genderTypes = ['Мужчина', 'Женщина']
emailTypes = ['Личный', 'Рабочий']
phoneTypes = ['Городской', 'Мобильный']

user = {}
email = {}
phone = {}

for _ in range(50):
    user['full_name'] = fake.name()
    user['birthdate'] = fake.date_of_birth(minimum_age=10)
    user['address'] = fake.address()
    user['gender'] = random.choice(genderTypes)
    cur = dbconn.cursor()
    postgres_insert_query = """ INSERT INTO users (full_name, birthdate, address, gender) VALUES (%s,%s,%s,%s)"""
    record_to_insert = (user['full_name'], user['birthdate'], user['address'], user['gender'])
    cur.execute(postgres_insert_query, record_to_insert)
    dbconn.commit()
    print("Record inserted successfully")

    email['user_id'] = _ + 1
    email['type'] = random.choice(emailTypes)
    email['email'] = fake.email()
    postgres_insert_query = """ INSERT INTO email (user_id, type, email) VALUES (%s,%s,%s)"""
    record_to_insert = (email['user_id'], email['type'], email['email'])
    cur.execute(postgres_insert_query, record_to_insert)
    dbconn.commit()

    phone['user_id'] = _ + 1
    phone['number_type'] = random.choice(phoneTypes)
    phone['number'] = fake.phone_number()
    postgres_insert_query = """ INSERT INTO phone_number (user_id, number_type, number) VALUES (%s,%s,%s)"""
    record_to_insert = (phone['user_id'], phone['number_type'], phone['number'])
    cur.execute(postgres_insert_query, record_to_insert)
    dbconn.commit()

dbconn.close()
