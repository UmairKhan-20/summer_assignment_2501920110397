# program to create student record system using arrays and strings
students = []
while True:
    print("    Student Record System    ")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_age = int(input("Enter student age: "))
        student = {"student_id": student_id, "student_name": student_name, "student_age": student_age}
        students.append(student)
    elif choice == 2:
        for s in students:
            print("Student ID:", s["student_id"], "Student Name:", s["student_name"], "Student Age:", s["student_age"])
    elif choice == 3:
        search=input("Enter student_id to search: ")
        found=False
        for s in students:
            if s["student_id"]==search:
                print("Student Found")
                print("Student ID:", s["student_id"], "Student Name:", s["student_name"], "Student Age:", s["student_age"])
                found=True
        if not found:
            print("Student not found")
    elif choice == 4:
        print("Exit")
        break
    else:
        print("Invalid choice")