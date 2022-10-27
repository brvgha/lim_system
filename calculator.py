# calculator module for the apex app

def calculator():
    n1 = int(input('\tPlease enter the first value: '))
    n2 = int(input('\tPlease enter the second value: '))
    func = str(input('\tPlease enter the operator: '))
    if func == '+':
        n3 = n1 + n2
        return n3
    if func == '-':
        n3 = n1 - n2
        return n3
    if func == 'x':
        n3 = n1 * n2
        return n3
    if func == '/':
        n3 = n1 / n2
        return n3
    if func == 'square':
        n3 = n1**n2
        return n3
    if func == 'root':
        n3 = n1**(1/n2)
        return n3
