from create_table import create_table
from register import register
from login import login
from start_screen import start_screen

l = True

while l:
    create_table()
    choice = input('\t\tDo you have an account: ')
    choice = choice.upper()
    yes_lst = ['YES', 'Y', 'YEAH', 'YE']
    no_lst = ['N', 'NO', 'NAY', 'NO WAY JOSE']
    quit_lst = ['Q', 'QUIT', 'EXIT']
    if choice in yes_lst:
        login()
        l = False
    elif choice in quit_lst:
        l = False
    elif choice in no_lst:
        print('****************************************************')
        newAccChoice = input(
            '******** '+'Would you like to make an account? ' + '********' + '\n\t\t\t')
        print('***************************************************')
        newAccChoice = newAccChoice.upper()
        if newAccChoice in yes_lst:
            register()
        else:
            l = False
    else:
        l = False