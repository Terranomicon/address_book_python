import random

import database
from faker import Faker

dbconn = database.get_connection()
fake = Faker('ru_RU')

genderTypes = ['Мужчина', 'Женщина']
emailTypes = ['Личный', 'Рабочий']
phoneTypes = ['Городской', 'Мобильный']

user_data, phone_data, email_data = [], [], []

for _ in range(50):
    user_tuple = (fake.name(), fake.date_of_birth(minimum_age=10), fake.address(), random.choice(genderTypes))
    user_data.append(user_tuple)

    email_tuple = (_ + 1, random.choice(emailTypes), fake.email())
    email_data.append(email_tuple)

    phone_tuple = (_ + 1, random.choice(phoneTypes), fake.phone_number())
    phone_data.append(phone_tuple)

cur = dbconn.cursor()
user_insert_query = """ INSERT INTO users (full_name, birthdate, address, gender) VALUES (%s,%s,%s,%s)"""
cur.executemany(user_insert_query, user_data)

email_insert_query = """ INSERT INTO email (user_id, type, email) VALUES (%s,%s,%s)"""
cur.executemany(email_insert_query, email_data)

phone_insert_query = """ INSERT INTO phone_number (user_id, number_type, number) VALUES (%s,%s,%s)"""
cur.executemany(phone_insert_query, phone_data)

dbconn.commit()
print("All data inserted successfully")
dbconn.close()
