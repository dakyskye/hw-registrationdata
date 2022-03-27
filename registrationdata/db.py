import os
import mysql.connector
from mysql.connector import MySQLConnection
from mysql.connector.cursor_cext import CMySQLCursor

from registrationdata.city import City
from registrationdata.user import User

_db: MySQLConnection
_cur: CMySQLCursor


def init():
    global _db
    global _cur
    _db = mysql.connector.connect(
        host=os.environ['MYSQL_HOST'],
        port=os.environ['MYSQL_PORT'],
        database=os.environ['MYSQL_DATABASE'],
        user=os.environ['MYSQL_USER'],
        password=os.environ['MYSQL_PASSWORD']
    )
    _cur = _db.cursor()

    for city in City:
        city = city.value
        _cur.execute(f"""
            INSERT INTO cities (name) SELECT '{city}' WHERE NOT EXISTS (SELECT null FROM cities WHERE name = '{city}')
        """)
    _db.commit()


def close():
    _db.commit()
    _db.close()


def __city_id(city: City) -> int:
    _cur.execute(f"SELECT id FROM cities WHERE name = '{city.value}'")
    return _cur.fetchall()[0][0]


def insert_user(user: User):
    _cur.execute(f"""
        INSERT INTO users (id, first_name, last_name, age, city)
        VALUES ('{user.uid}', '{user.first_name}', '{user.last_name}', {user.age}, {__city_id(user.city)})
    """)
    _db.commit()
