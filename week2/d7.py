

def password_validate(password) :
    digit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    if len(password)<8:
        return False
    else :
        for char in password:
            if char.isdigit() not in digit:
                return False
            else:
                for char in password:
                    if not any(char.isupper()):
                        return False
                    else:
                        return True



#print(password_validate('Myww2game'))

def common(list1,list2):
    arr = []
    for item in list1 :
        if item in list2:
            arr.append(item)

    return arr
print(common([1,2,3,4,5],[4,5,6,7]))
