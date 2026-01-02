list1 = []
id3 = 1
while True :
    ask = input('Add a new student : ')
    age = int(input('Enter Age : '))
    grade = int(input('Enter Grade : '))
    marks = float(input('Enter Marks : '))
    print('id is',id3)
    des = input('Do you want to add another student ? : (yes/no)')
    student = {'name' : ask,
               'id' : id3,
               'age' : age,
               'grade' : grade,
               'marks' : marks,
               }
    id3 +=1
    list1.append(student)
    if des.lower().strip() == 'yes' :
        continue
    else :
        break
a = True
while a:
    print('1• Add a new student ')
    print('2• Display all students')
    print('3• Search student by ID ')
    print('4• Update student information')
    print('5• Delete a student record')
    print('6• Exit the program')
    option = int(input('Enter your choice : '))
    list2=[option]
    for option in list2 :

        if option == 1:
            ask = input('Add a new student : ')
            age = int(input('Enter Age : '))
            grade = int(input('Enter Grade : '))
            marks = float(input('Enter Marks : '))
            print('id is', id3)
            des = input('Do you want to add another student ? : (yes/no)')
            student = {'name': ask,
                       'id': id3,
                       'age': age,
                       'grade': grade,
                       'marks': marks,}
            list1.append(student)
            id3 +=1
            if des.lower().strip() == 'yes':
                continue
            elif des.lower().strip() == 'no':
                o = input('Do you want to exit the program ? : (yes/no)')

                if o.lower().strip() == 'yes' :
                    break
                else :
                    continue

        if option == 2:
            print(list1)
            o = input('Do you want to exit the program ? : (yes/no)')
            if o.lower().strip() == 'yes':
                break
            else:
                continue
        if option == 3:
            id2 = int(input('Enter STUDENT_ID : '))
            for student in list1:
                if student['id'] == id2 :
                    print(student)
                else :
                    print('input invalid')
            o = input('Do you want to exit the program ? : (yes/no)')
            if o.lower().strip() == 'yes':
                break
            else:
                continue
        if option == 4:
            id2 = int(input('Enter STUDENT_ID : '))
            for student in list1:
                if student['id'] == id2:
                    print(student)
                    change = input('What do you want to change?')
                    if change.lower().strip() == 'name' :
                        change = input('Enter new name : ')
                        student['name'] = change
                    elif change.lower().strip() == 'id' :
                        change = input('Enter new id : ')
                        student['id'] = change
                    elif change.lower().strip() == 'age' :
                        change = input('Enter new age : ')
                        student['age'] = change
                    elif change.lower().strip() == 'grade' :
                        change = input('Enter new grade : ')
                        student['grade'] = change
                    elif change.lower().strip() == 'marks' :
                        change = input('Enter new marks : ')
                        student['marks'] = change
                else:
                    print('input invalid')
            o = input('Do you want to exit the program ? : (yes/no)')
            if o.lower().strip() == 'yes':
                break
            else:
                continue
        if option == 5:
            id2 = int(input('Enter STUDENT_ID : '))
            for student in list1:
                if student['id'] == id2:
                    list1.remove(student)
            o = input('Do you want to exit the program ? : (yes/no)')
            if o.lower().strip() == 'yes':
                break
            else:
                continue
        if option == 6 :
            a = False




