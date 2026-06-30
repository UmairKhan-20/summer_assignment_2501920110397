# program to create mini employee management system
emp=[]
while True:
    print("     Mini employee management system     ")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Delete Employee")
    print("4. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        name=input("Enter Employee name: ")
        emp.append(name)
    elif choice==2:
        print("Employees:")
        for i in emp:
            print(i)
    elif choice==3:
        name=input("Enter Employee name to Delete: ")
        if name in emp:
            emp.remove(name)
            print("Employee Deleted")
        else:
            print("Employee not Found")
    elif choice==4:
        print("Exit")
        break
    else:
        print("Invalid choice") 
    
    
    
    
    
    
    
    
    
    
    
