price = 25
quantity = 4
tax_rate = 0.15

subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print(f"Subtotal: {subtotal:.2f} SAR")
print(f"Tax:      {tax:.2f} SAR")
print(f"Total:    {total:.2f} SAR")