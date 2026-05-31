balance = 200

print("1 - Check balance")
print("2 - Deposit 100 SAR")
print("3 - Withdraw 50 SAR")
print("4 - Exit")

choice = input("Enter your choice: ")

match choice:
    case "1":
        print("Current balance:", balance)

    case "2":
        balance += 100
        print("New balance:", balance)

    case "3":
        if balance >= 50:
            balance -= 50
            print("New balance:", balance)
        else:
            print("Insufficient funds")

    case "4":
        print("Goodbye!")

    case _:
        print("Invalid choice")