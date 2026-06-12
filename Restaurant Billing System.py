menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popcorn": 6.00,
    "fries": 2.50,
    "chips": 1.00,
    "pretzel": 3.50,
    "soda": 3.00,
    "lemonade": 4.25
}

cart = {}
subtotal = 0

print("\n========== MENU ==========")

for item, price in menu.items():
    print(f"{item:<10} : ${price:.2f}")

print("==========================")

while True:
    food = input("\nSelect an item (q to quit): ").lower()

    if food == "q":
        break

    if food not in menu:
        print("Item not found in menu!")
        continue

    quantity = (input(f"Enter quantity of {food}: "))

    if food in cart:
        cart[food] += quantity
    else:
        cart[food] = quantity

print("\n========== RECEIPT ==========")

for food, quantity in cart.items():
    item_total = menu[food] * int(quantity)
    subtotal += item_total

    print(
        f"{food.capitalize():<10} x {quantity:<3}"
        f"= ${item_total:.2f}"
    )

tax_rate = 0.18  # 18% GST
tax = subtotal * tax_rate
grand_total = subtotal + tax

print("-----------------------------")
print(f"Subtotal      : ${subtotal:.2f}")
print(f"GST (18%)     : ${tax:.2f}")
print(f"Grand Total   : ${grand_total:.2f}")
print("=============================")

# Save receipt to file
with open("receipt.txt", "w") as file:
    file.write("====== RECEIPT ======\n")

    for food, quantity in cart.items():
        item_total = menu[food] * int(quantity)
        file.write(
            f"{food.capitalize()} x {quantity} = ${item_total:.2f}\n"
        )

    file.write("----------------------\n")
    file.write(f"Subtotal : ${subtotal:.2f}\n")
    file.write(f"GST      : ${tax:.2f}\n")
    file.write(f"Total    : ${grand_total:.2f}\n")

print("\nReceipt saved successfully as 'receipt.txt'")


**OUTPUT
========== MENU ==========
pizza      : $3.00
nachos     : $4.50
popcorn    : $6.00
fries      : $2.50
chips      : $1.00
pretzel    : $3.50
soda       : $3.00
lemonade   : $4.25
==========================

Select an item (q to quit): pizza
Enter quantity of pizza: 2

Select an item (q to quit): chips
Enter quantity of chips: 1

Select an item (q to quit): fries
Enter quantity of fries: 2

Select an item (q to quit): q

========== RECEIPT ==========
Pizza      x 2  = $6.00
Chips      x 1  = $1.00
Fries      x 2  = $5.00
-----------------------------
Subtotal      : $12.00
GST (18%)     : $2.16
Grand Total   : $14.16
=============================

Receipt saved successfully as 'receipt.txt'
