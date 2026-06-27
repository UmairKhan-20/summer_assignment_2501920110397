# program to create marksheet generation system
marksheets = []
while True:
    print("    Marksheet Generation System    ")
    print("1. Add Marksheet")
    print("2. View Marksheets")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter student name: ")
        subject = input("Enter subject: ")
        marks = float(input("Enter marks: "))
        marksheet = {"name": name, "subject": subject, "marks": marks}
        marksheets.append(marksheet)
    elif choice == 2:
        for m in marksheets:
            print("Name:", m["name"], "Subject:", m["subject"], "Marks:", m["marks"])
    elif choice == 3:
        print("Exit")
        break
    else:
        print("Invalid choice")