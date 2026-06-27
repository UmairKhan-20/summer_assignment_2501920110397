# program to create student record management system
students = []
while True:
    print("    Student Record Management System    ")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        grade = input("Enter student grade: ")
        student = {"name": name, "age": age, "grade": grade}
        students.append(student)
    elif choice == 2:
        for s in students:
            print("Name:", s["name"], "Age:", s["age"], "Grade:", s["grade"])
    elif choice == 3:
        print("Exit")
        break
    else:
        print("Invalid choice")
