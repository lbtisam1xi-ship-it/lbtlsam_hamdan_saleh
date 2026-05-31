total = 287

coins_100 = total // 100
remaining = total % 100

coins_50 = remaining // 50
remaining = remaining % 50

coins_25 = remaining // 25
remaining = remaining % 25

coins_10 = remaining // 10
remaining = remaining % 10

coins_5 = remaining // 5
remaining = remaining % 5

coins_1 = remaining // 1

print("Total halalas:", total)

print("100-halala coins:", coins_100)
print("50-halala coins:", coins_50)
print("25-halala coins:", coins_25)
print("10-halala coins:", coins_10)
print("5-halala coins:", coins_5)
print("1-halala coins:", coins_1)