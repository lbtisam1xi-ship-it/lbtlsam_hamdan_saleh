age = int(input("Enter age: "))
day = input("Enter day: ")

if age < 12:
    price = 20
else:
    if age <= 17:
        price = 35
    else:
        if age <= 59:
            price = 50
        else:
            price = 25

if day == "Tuesday":
    price = price - 10
    if price < 10:
        price = 10

print("Final ticket price:", price, "SAR")