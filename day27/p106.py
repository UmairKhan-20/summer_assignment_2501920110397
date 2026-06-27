# program to create employee management system
employees = []
while True:
    print("    Employee Management System    ")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter employee name: ")
        age = int(input("Enter employee age: "))
        employee_id = input("Enter employee ID: ")
        employee = {"name": name, "age": age, "employee_id": employee_id}
        employees.append(employee)
    elif choice == 2:
        for e in employees:
            print("Name:", e["name"], "Age:", e["age"], "Employee ID:", e["employee_id"])
    elif choice == 3:
        print("Exit")
        break
    else:
        print("Invalid choice")