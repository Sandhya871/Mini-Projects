history = []

while True:
    print("\n===== CALCULATOR =====")
    print("Available operators: +  -  *  /  %  ^")
    print("Enter 'q' to quit")

    operator = input("Enter an operator: ")

    if operator.lower() == "q":
        break

    if operator not in ["+", "-", "*", "/", "%", "^"]:
        print("Invalid operator!")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Cannot divide by zero!")
            continue
        result = num1 / num2
    elif operator == "%":
        result = num1 % num2
    elif operator == "^":
        result = num1 ** num2

    print(f"Result: {round(result, 3)}")

    history.append(f"{num1} {operator} {num2} = {result}")

print("\n===== CALCULATION HISTORY =====")
for item in history:
    print(item)

print("Thank you for using the calculator!")


A menu-driven Python calculator that performs arithmetic operations, handles errors, supports calculation history, 
and allows multiple calculations in a single session.

# OUTPUT
===== CALCULATOR =====
Available operators: +  -  *  /  %  ^
Enter 'q' to quit
Enter an operator: +
Enter first number: 12
Enter second number: 13
Result: 25.0

===== CALCULATOR =====
Available operators: +  -  *  /  %  ^
Enter 'q' to quit
Enter an operator: -
Enter first number: 12
Enter second number: 13
Result: -1.0

===== CALCULATOR =====
Available operators: +  -  *  /  %  ^
Enter 'q' to quit
Enter an operator: *
Enter first number: 12
Enter second number: 13
Result: 156.0

===== CALCULATOR =====
Available operators: +  -  *  /  %  ^
Enter 'q' to quit
Enter an operator: /
Enter first number: 12
Enter second number: 13
Result: 0.923

===== CALCULATOR =====
Available operators: +  -  *  /  %  ^
Enter 'q' to quit
Enter an operator: %
Enter first number: 12
Enter second number: 13
Result: 12.0

===== CALCULATOR =====
Available operators: +  -  *  /  %  ^
Enter 'q' to quit
Enter an operator: ^
Enter first number: 12
Enter second number: 13
Result: 106993205379072.0

===== CALCULATOR =====
Available operators: +  -  *  /  %  ^
Enter 'q' to quit
Enter an operator: q

===== CALCULATION HISTORY =====
12.0 + 13.0 = 25.0
12.0 - 13.0 = -1.0
12.0 * 13.0 = 156.0
12.0 / 13.0 = 0.9230769230769231
12.0 % 13.0 = 12.0
12.0 ^ 13.0 = 106993205379072.0
Thank you for using the calculator!
