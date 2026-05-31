inventory = {"laptop": 5, "mouse": 10, "keyboard": 0}

orders = [
    ("laptop", 2),
    ("mouse", 15),
    ("keyboard", 1),
    ("monitor", 3),
]

for product, qty in orders:
    match product:
        case p if p not in inventory:
            print(f"{product}: not in inventory")

        case p if inventory[p] >= qty:
            inventory[p] -= qty
            print(f"{product}: shipped {qty}, {inventory[p]} left")

        case p:
            print(f"{product}: only {inventory[p]} in stock, cannot ship {qty}")