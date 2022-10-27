# attempt to recreate apex interface
from calculator import calculator


def start_screen():
    quit_list = ['q', 'quit', 'exit']
    options = ['Calculator', 'option 2', 'option 3', 'option 4',
               'option 5', 'option 6', 'option 7', 'option 8', ]
    l = True
    while l:
        print('\t Please choose an option below:')
        print('\n' + 'Calculator' + '\toption 2' + '\toption 3' + '\toption 4' +
              '\n' + '\noption 5' + '\toption 6' + '\toption 7' + '\toption 8')
        choice = input('\n\tPlease enter your choice here: ')

        if (choice not in quit_list) and (choice in options):
            print('\t\tYou chose {}'.format(choice))
            for x in options:
                if x == 'Calculator':
                    answer = calculator()
                    print(f'\tThe answer is: {answer}')

        elif (choice not in quit_list) and (choice not in options):
            print('That option is not available, please try again.')

        else:
            print('\t\tGoodbye')
            l = False
