# program to create bank account system
accounts = []
while True:
    print("    Bank Account System    ")
    print("1. Create Account")
    print("2. View Accounts")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        account_number = input("Enter account number: ")
        account_holder = input("Enter account holder name: ")
        balance = int(input("Enter initial balance: "))
        account = {"account_number": account_number, "account_holder": account_holder, "balance": balance}
        accounts.append(account)
    elif choice == 2:
        for a in accounts:
            print("Account Number:", a["account_number"], "Account Holder:", a["account_holder"], "Balance:", a["balance"])
    elif choice == 3:
        account_number = input("Enter account number: ")
        amount = int(input("Enter amount to deposit: "))
        for a in accounts:
            if a["account_number"] == account_number:
                a["balance"] += amount
                print("Deposit successful. New balance:", a["balance"])
    elif choice == 4:
        account_number = input("Enter account number: ")
        amount = int(input("Enter amount to withdraw: "))
        for a in accounts:
            if a["account_number"] == account_number:
                if a["balance"] >= amount:
                    a["balance"] -= amount
                    print("Withdrawal successful. New balance:", a["balance"])
                else:
                    print("Insufficient balance")
    elif choice == 5:
        print("Exit")
        break
    else:
        print("Invalid choice")
    
