
balance = 10000.00

print("Welcome to Kiran Bank")
print("Opening Balance: Rs.", format(balance, ".2f"))

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Current Balance: Rs.", format(balance, ".2f"))

    elif choice == "2":
        try:
            amount = float(input("Enter deposit amount: "))

            if amount <= 0:
                print("Invalid amount. Deposit must be greater than zero.")
            else:
                balance += amount
                print("Deposit successful.")
                print("Updated Balance: Rs.", format(balance, ".2f"))

        except ValueError:
            print("Invalid amount. Please enter a valid number.")

    elif choice == "3":
        try:
            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Invalid amount. Withdrawal must be greater than zero.")
            elif amount > balance:
                print("Transaction failed: Insufficient balance.")
                print("Current Balance: Rs.", format(balance, ".2f"))
            else:
                balance -= amount
                print("Withdrawal successful.")
                print("Updated Balance: Rs.", format(balance, ".2f"))

        except ValueError:
            print("Invalid amount. Please enter a valid number.")

    elif choice == "4":
        print("Thank you for banking with us. Goodbye!")
        break

    else:
        print("Invalid choice. Please select an option from 1 to 4.")
