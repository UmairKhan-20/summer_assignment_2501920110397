# program to create menu-driven calculator
while True:
    print("    Menu-Driven Calculator    ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 + num2
        print("Result:", result)
    elif choice == 2:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 - num2
        print("Result:", result)
    elif choice == 3:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 * num2
        print("Result:", result)
    elif choice == 4:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 != 0:
            result = num1 / num2
            print("Result:", result)
        else:
            print("Error: Division by zero is not allowed.")
    elif choice == 5:
        print("Exit")
        break
    else:
        print("Invalid choice")