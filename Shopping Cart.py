foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower()=="q":
        break
    else:
        price = float(input(f"Enter a price of {food}: Rs "))
        foods.append(food)
        prices.append(price)

print('---- YOUR CART ----')
for food in foods:
    print(food,end = "  ")
for price in prices:
    total= total + price
print()
print(f"Your total price is : Rs {total}")

'''A Python shopping cart application that allows users to 
   add food items, track prices, and calculate the total bill.'''

# OUTPUT
Enter a food to buy (q to quit): pizza
Enter a price of pizza: Rs 180
Enter a food to buy (q to quit): fries
Enter a price of fries: Rs 80
Enter a food to buy (q to quit): chips
Enter a price of chips: Rs 49
Enter a food to buy (q to quit): nuggets
Enter a price of nuggets: Rs 150
Enter a food to buy (q to quit): q
---- YOUR CART ----
pizza  fries  chips  nuggets  
Your total price is : Rs 459.0
