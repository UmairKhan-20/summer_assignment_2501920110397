# program to create salary management system
salaries = []
while True:
    print("    Salary Management System    ")
    print("1. Add Salary")
    print("2. View Salaries")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter employee name: ")
        salary_amount = float(input("Enter salary amount: "))
        salary = {"name": name, "salary_amount": salary_amount}
        salaries.append(salary)
    elif choice == 2:
        for s in salaries:
            print("Name:", s["name"], "Salary Amount:", s["salary_amount"])
    elif choice == 3:
        print("Exit")
        break
    else:
        print("Invalid choice")