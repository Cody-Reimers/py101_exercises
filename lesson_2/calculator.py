print("Welcome to calculator.py!")
print("Please use raw numbers with no formatting, and the following "
    "operators are supported:\n\"+\" (addition), \"-\" (subtraction), "
    "\"*\" (multiplication), \"/\" (division)\n"
    "You can quit at any time by entering \"quit\" as any input.")

while True:
    num1 = input("What's the first number? ")
    if num1 == "quit":
        break
    
    num2 = input("What's the second number? ")
    if num2 == "quit":
        break
    
    if num1.isnumeric() and num2.isnumeric():
        num1 = int(num1)
        num2 = int(num2)
    else:
        print("That input won't work!")
        continue
    
    operator = input("What operation do you want to perform? ")
    
    if operator == "quit":
        break
    elif operator == "+":
        output = num1 + num2
    elif operator == "-":
        output = num1 - num2
    elif operator == "*":
        output = num1 * num2
    elif operator == "/":
        output = num1 // num2
    else:
        print("That input won't work!")
    
    print(f"{num1} {operator} {num2} = {output}")

print("Thank you for running calculator.py!")