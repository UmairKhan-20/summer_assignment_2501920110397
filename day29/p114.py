# program to create menu-driven array operations system
arr=[]
while True:
    print("    Menu-Driven Array Operations System    ")
    print("1. Add Element")
    print("2. View Elements")
    print("3. Search Element")
    print("4. Delete Element")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        num = int(input("Enter element to add: "))
        arr.append(num)
    elif choice == 2:
        print("Elements in the array:", arr)
    elif choice == 3:
        search=int(input("Enter element to search: "))
        if search in arr:
            print("Element found")
        else:
            print("Element not found")
    elif choice == 4:
        delete=int(input("Enter element to delete: "))
        if delete in arr:
            arr.remove(delete)
            print("Element deleted")
        else:
            print("Element not found")
    elif choice == 5:
        print("Exit")
        break
    else:
        print("Invalid choice")