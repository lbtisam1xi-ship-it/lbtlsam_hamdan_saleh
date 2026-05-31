readings = [-5, 10, 25, 40]

for temp in readings:

    if temp < 0:
        print(f"{temp}°C: Freezing")

    elif temp <= 19:
        print(f"{temp}°C: Cold")

    elif temp <= 34:
        print(f"{temp}°C: Warm")

    else:
        print(f"{temp}°C: Hot")