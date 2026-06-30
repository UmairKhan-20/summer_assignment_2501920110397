# program to create library management system
library = []
while True:
    print("    Library Management System    ")
    print("1. Add Book")
    print("2. View Books")
    print("3. search Book")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        book_id = input("Enter book ID: ")
        book_name = input("Enter book name: ")
        author = input("Enter author name: ")
        book = {"book_id": book_id, "book_name": book_name, "author": author}
        library.append(book)
    elif choice == 2:
        for b in library:
            print("Book ID:", b["book_id"], "Book Name:", b["book_name"], "Author:", b["author"])
    elif choice == 3:
        search=input("Enter book_id to search: ")
        found=False
        for b in library:
            if b["book_id"]==search:
                print("Book Found")
                print("Book ID:", b["book_id"], "Book Name:", b["book_name"], "Author:", b["author"])
                found=True
        if not found:
            print("Book not found")
    elif choice == 4:
        print("Exit")
        break
    else:
        print("Invalid choice")