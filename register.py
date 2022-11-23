import sqlite3
import getpass

from encrypt_pass import encrypt_pass


def register():
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()

    try:
        cursor.execute('INSERT INTO users VALUES(?,?,?,?,?)',
                       ('1000', 'Dummy', 'Dummy', 'Dummy', 'dummy101'))

    except:
        pass

    # takes the new account details from the user
    user = input('Please enter your username: ')
    forename = input('Please enter your forename: ')
    surname = input('Please enter your surname: ')
    password = getpass.getpass('Please enter your password: ')
    while len(password) < 8:
        password = getpass.getpass('Please enter your password: ')

    password, char_lst, encrypt_lst = encrypt_pass(password)

    # checks last entry into table for their ID and adds 1
    cursor.execute('SELECT id FROM users;')
    result = cursor.fetchall()
    last = result[-1]
    res = int(''.join(map(str, last)))
    res += 1

    # this checks to make sure the user is not already in the database
    cursor.execute('SELECT user FROM users;')
    table = cursor.fetchall()
    check = False
    for i in range(len(table)):
        if user == table[i][0]:
            check = True

    if not check:
        cursor.execute('INSERT INTO users VALUES(?,?,?,?,?);',
                       (res, user, forename, surname, password))
        connection.commit()
        connection.close()

    else:
        print('User already exists')
        connection.commit()
        connection.close()
