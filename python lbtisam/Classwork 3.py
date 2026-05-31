first = int(input("First: "))
second = int(input("Second: "))
third = int(input("Third: "))

if first >= second and first >= third:
    print("The largest is", first)

elif second >= first and second >= third:
    print("The largest is", second)

else:
    print("The largest is", third)