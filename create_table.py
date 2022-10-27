import sqlite3


def create_table():

    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, user TEXT, forename TEXT, surname TEXT, password TEXT);')
    connection.commit()
    connection.close()


create_table()