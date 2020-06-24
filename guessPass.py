# ClickCyber Python 
def encryptions(string):
    secret = []
    global all
    for forAll in range(len(string)):
       for i in all:
            if string[forAll] == i:
                secret.append(i)
            elif not(string[forAll] in all):
                all.append(string[forAll])
                print(f'add new element {string[forAll]}')
    secret = "".join(secret)
    return(secret)

all = ['a','b','c','d']
key = input('Enetr Your password\n')
say = encryptions(key)
result = say == key
print (f'Is the result correct? {result}\nYour string: {key}\nreturn: {say}')