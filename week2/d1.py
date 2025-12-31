my_dictionary = {'key1' : 'Devansh', 'key2' : 'Taparia', 'key3' : 13}
print(f"My name is {my_dictionary['key1'],my_dictionary['key2']} and I am {my_dictionary['key3']} years old ")
my_dictionary = {
                'firstname': 'Devansh',
                'lastname':'Taparia',
                'age': '13'
                }
for key in my_dictionary:
    if key == 'firstname':
        print(key,my_dictionary['firstname'])

    elif key == 'lastname':
        print(key,my_dictionary['lastname'])

    else:
        print(key,my_dictionary['age'])
