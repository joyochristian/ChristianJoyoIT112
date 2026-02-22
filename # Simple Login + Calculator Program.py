# Simple Login + Calculator Program

# Predefined username and password
USERNAME = "admin"
PASSWORD = "1234"

print("=== Welcome to Secure Calculator ===")

# Login system
username = input("Enter username: ")
password = input("Enter password: ")

if username == USERNAME and password == PASSWORD:
    print("\nLogin successful!\n")
    
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")

        if choice == "5":
            print("Goodbye!")
            break
        
        if choice in ("1", "2", "3", "4"):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == "1":
                    print("Result:", num1 + num2)
                elif choice == "2":
                    print("Result:", num1 - num2)
                elif choice == "3":
                    print("Result:", num1 * num2)
                elif choice == "4":
                    if num2 != 0:
                        print("Result:", num1 / num2)
                    else:
                        print("Error: Cannot divide by zero.")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        else:
            print("Invalid choice. Please select 1-5.")
else:
    print("Login failed. Incorrect username or password.")