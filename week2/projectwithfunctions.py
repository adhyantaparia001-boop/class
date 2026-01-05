students = {}
next_id = 1

def add_student():
    next_id = 1
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    grade = int(input("Enter Grade: "))
    marks = float(input("Enter Marks: "))
    students[next_id] = {
        "name": name,
        "age": age,
        "grade": grade,
        "marks": marks
    }
    print(f" Student added with ID {next_id}")
    next_id += 1

def display_students():
    if students:
        for sid, info in students.items():
            print(f"ID {sid}: {info}")
    else:
        print("️ No students found.")

def search_student():
    sid = int(input("Enter STUDENT_ID: "))
    print(students.get(sid, " Student not found."))

def update_student():
    sid = int(input("Enter STUDENT_ID: "))
    if sid in students:
        print("Current record:", students[sid])
        field = input("What do you want to change? (name/age/grade/marks): ").lower()
        if field in students[sid]:
            new_value = input(f"Enter new {field}: ")
            if field in ["age", "grade"]:
                new_value = int(new_value)
            elif field == "marks":
                new_value = float(new_value)
            students[sid][field] = new_value
            print(" Record updated:", students[sid])
        else:
            print("️ Invalid field.")
    else:
        print("️ Student not found.")

def delete_student():
    sid = int(input("Enter STUDENT_ID: "))
    if students.pop(sid, None):
        print(" Student deleted.")
    else:
        print(" Student not found.")

# Main loop
while True:

    print("1. Add a new student")
    print("2. Display all students")
    print("3. Search student by ID")
    print("4. Update student information")
    print("5. Delete a student record")
    print("6. Exit the program")

    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print(" Exiting program...")
        break
    else:
        print(" Invalid choice. Try again.")