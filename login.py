import sqlite3
from encrypt_pass import encrypt_pass
from register import register
import getpass
from start_screen import start_screen

yes_lst = ['Y', 'YES']


def login():

    user = input('Please enter your username: ')
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute('SELECT user FROM users')
    table = cursor.fetchall()

    try:
        l = True
        count = 0
        while l:
            for i in table:
                if user == i[0]:
                    password = getpass.getpass('Please enter your password: ')
                    password, char_lst, encrypt_lst = encrypt_pass(password)
                    cursor.execute(
                        'SELECT password FROM users WHERE user="{}"'.format(user))
                    res = cursor.fetchall()
            if password == res[0][0]:
                start_screen()
                l = False
            else:
                print('Incorrect password entered.')
            if count == 2:
                print(
                    'You have entered the password incorrectly three times. Your account is locked')
                l = False
            else:
                count += 1

    except UnboundLocalError:
        question = input('Account not found, would you like to register?: ')
        question = question.upper()
        if question in yes_lst:
            register()
        else:
            print('Goodbye')
