# python program to encrypt password

def encrypt_pass(password):
    char_lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7',
                '8', '9', '0']

    for i in char_lst[0:26]:
        char_lst.append(i.upper())

    encryptLst = list(range(1, len(char_lst)+1))

    for n in range(len(encryptLst)):
        if len(str(encryptLst[n])) == 1:
            encryptLst[n] = '0' + str(encryptLst[n])

    encryptedPass = ''

    for i in password:
        if i in char_lst:
            pos = char_lst.index(i)
            encryptedPass += str(encryptLst[pos])

    return encryptedPass, char_lst, encryptLst
