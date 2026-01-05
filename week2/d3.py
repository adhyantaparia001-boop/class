 #def name(firstname,lastname):

    #print(firstname+' '+lastname)

#name(firstname=str(input ('Enter your name:')),lastname=str(input ('Enter your last name:')))


def name(firstname, lastname):
    return firstname + ' ' + lastname
num = name(firstname=str(input('Enter your name:')), lastname=str(input('Enter your last name:')))
print(num)

