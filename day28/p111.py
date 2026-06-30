# program to create ticket booking system
tickets = []
while True:
    print("    Ticket Booking System    ")
    print("1. Book Ticket")
    print("2. View Tickets")
    print("3. Search Ticket")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        ticket_id = input("Enter ticket ID: ")
        passenger_name = input("Enter passenger name: ")
        destination = input("Enter destination: ")
        ticket = {"ticket_id": ticket_id, "passenger_name": passenger_name, "destination": destination}
        tickets.append(ticket)
    elif choice == 2:
        for t in tickets:
            print("Ticket ID:", t["ticket_id"], "Passenger Name:", t["passenger_name"], "Destination:", t["destination"])
    elif choice == 3:
        search=input("Enter ticket_id to search: ")
        found=False
        for t in tickets:
            if t["ticket_id"]==search:
                print("Ticket Found")
                print("Ticket ID:", t["ticket_id"], "Passenger Name:", t["passenger_name"], "Destination:", t["destination"])
                found=True
        if not found:
            print("Ticket not found")
    elif choice == 4:
        print("Exit")
        break
    else:
        print("Invalid choice")