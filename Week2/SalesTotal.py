# Total Purchase

# Wite a program that calculates the total of five items
# Display sub-total, sales tax (7 percent), and the total.

cart = []
cartLimit = range(5)
tax = .07
subtotal = 0
total = 0

for x in cartLimit:
    cart.append(input(f'What is the cost of item {x+1}? '))

for x in range(0, len(cart)):
    subtotal = subtotal + int(cart[x])

for index, value in enumerate(cart):
    cart[index] = int(value)*tax + int(value)

for x in range(0, len(cart)):
    total = float(total) + float(cart[x])

print(f"Your subtotal is {subtotal}")
print(f"Your total sales tax is {float(total) - float(subtotal)}")
print(f"Your total is {total}")

# Still struggling to get the decimal numbers to add correctly..
# will need to look more into that

