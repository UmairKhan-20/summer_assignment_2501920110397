# program to create ATM simulation system
balance = 100000
print("   Welcome to the ATM Simulation System   ")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")
choice = int(input("Enter your choice (1-4): "))
if choice == 1:
    print("Your current balance is:", balance)
elif choice == 2:
    amount=int(input("Enter the amount to deposit: "))
    balance += amount
    print("Amount deposited successfully.")
    print("Updated balance is:", balance)
elif choice == 3:
    amount=int(input("Enter the amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print("Amount withdrawn successfully.")
        print("Updated balance is:", balance)
    else:
        print("Insufficient balance.")
elif choice == 4:
    print("Thank you for using the ATM Simulation System.")
else:
    print("Invalid choice")