a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

match operator:
    case "+":
        print(a + b)

    case "-":
        print(a - b)

    case "*":
        print(a * b)

    case "/":
        if b == 0:
            print("Error: division by zero")
        else:
            print(a / b)

    case _:
        print("Unknown operator")