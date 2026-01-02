#my_list = [1,2,3,4,5,6,7,8,9]
#print(my_list[5:9])
info ={
   'class_name' : '',
'class_no': '',
    'class_area': '',
    'class_availability' :'',
    'students':' []'
}
class_name=input("Enter your class name :")
class_no = int(input("Enter your class number :"))
class_area =float(input("Enter your class area:"))
class_availability = bool(input("Enter your class availability(true/false):"))
students = []
while True :
    student = input("Enter your student name")
    students.append(student)
    des = input('do you want to continue(yes/no)?')
    if des.strip().lower() == 'no' :
         break
    elif des.strip().lower() == 'yes' :
         continue
    else :
        print("input invaild")
        intt = input('do you want to continue(yes/no)?')
if class_availability ==True:
    class_availability = 'yes'
    info["class_availability"] = class_availability
elif class_availability ==False:
    class_availabilty = 'no'
    info["class_availability"] = class_availability

info["class_name"] = class_name
info["class_no"] = class_no
info["class_area"] = class_area

info["students"] = students
for key in info :
    if key =='class_name' :
        print(key)
        print(info['class_name'])
    if  key =='class_no' :
        print(key)
        print(info['class_no'])
    if key =='class_area' :
        print(key)
        print(info['class_area'])
    if key =='students' :
        print(key)
        print(info['students'])
    if key =='class_availability' :
        print(key)
        print(info['class_availability'])



