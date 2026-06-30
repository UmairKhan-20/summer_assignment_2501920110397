# program to create contact management system
contacts = []
while True:
    print("    Contact Management System    ")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        contact_id = input("Enter contact ID: ")
        contact_name = input("Enter contact name: ")
        contact_number = input("Enter contact number: ")
        contact = {"contact_id": contact_id, "contact_name": contact_name, "contact_number": contact_number}
        contacts.append(contact)
    elif choice == 2:
        for c in contacts:
            print("Contact ID:", c["contact_id"], "Contact Name:", c["contact_name"], "Contact Number:", c["contact_number"])
    elif choice == 3:
        search=input("Enter contact_id to search: ")
        found=False
        for c in contacts:
            if c["contact_id"]==search:
                print("Contact Found")
                print("Contact ID:", c["contact_id"], "Contact Name:", c["contact_name"], "Contact Number:", c["contact_number"])
                found=True
        if not found:
            print("Contact not found")
    elif choice == 4:
        print("Exit")
        break
    else:
        print("Invalid choice")