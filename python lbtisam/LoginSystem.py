correct_password = "1234"


for attempt in range(1, 4):
    password = input(f"Enter password (attempt {attempt}): ")

    if password == correct_password:
        print(f"Access granted on attempt {attempt}")
        break
    else:
        if attempt < 3:
            print("Wrong password, try again")
        else:
            print("Account locked")