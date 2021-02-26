# address_book_python

# Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API](#api)

## Installation

```sh
git clone https://github.com/Terranomicon/address_book_python.git
```

Creating virtual environment (in project used Python 3.7)

```
python3 -m venv /path/to/new/virtual/environment
```

Install requirements

```
pip install -r requirements.txt
```
SQL schema (PostgreSQL 13)
```
schema.sql
```

Add config.ini as default.config.ini

```
configure config.ini
```

Script for filling the database

```
python3 seed.py
```

## Usage
Start app form "app" directory
```
flask run
```
## API
Default API urls
```
localhost:5000/
```
localhost:5000/user
```
get all users [POST]
    without params
get user by id [POST]
    id - int user id
create user [PUT]
    full_name - str user name
    birthdate - date user birthdate (yyyy-mm-dd)
    address - str user address
    gender - str user gender
update user [PATCH] (required only id)
    full_name - str user name
    birthdate - date user birthdate (yyyy-mm-dd)
    address - str user address
    gender - str user gender
    id - int user id
delete user [DELETE]
    id - int user id
```
localhost:5000/phone
```
get all phones [POST]
    without params
get phone by user id [POST]
    user_id - int user id
create phone [PUT]
    user_id - int user id
    number_type - str phone number type
    number - str phone number
update phone [PATCH] (required only user_id)
    user_id - int user id
    number_type - str phone number type
    number - str phone number
delete phone [DELETE]
    user_id - int user id
```
localhost:5000/email
```
get all emails [POST]
    without params
get email by user id [POST]
    user_id - int user id
create email [PUT]
    user_id - int user id
    type - str email type
    email - str email
update phone [PATCH] (required only user_id)
    user_id - int user id
    type - str email type
    email - str email
delete phone [DELETE]
    user_id - int user id
```
