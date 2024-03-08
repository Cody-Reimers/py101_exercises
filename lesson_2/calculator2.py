def user_prompt():
    return input("==> ")

def get_int():
    integer = user_prompt()
    if not integer.isnumeric():
        print("That input won't work; it must be an integer.")
        integer = get_int()
    return int(integer)

def get_operator():
    operator = user_prompt()
    valid_operators = ["+", "-", "*", "/"]
    if operator not in valid_operators:
        print("That input won't work; you must "
            "enter \"+\", \"-\", \"*\", or \"/\"")
        operator = get_operator()
    return operator

print("~~~~~~~~~~Welcome to calculator.py!~~~~~~~~~~")
print("""
    Please use raw numbers with no formatting,
    the following operators are supported:
    "+" (addition), "-" (subtraction), 
    "*" (multiplication), "/" (division)
"""
)

while True:
    print("What's the first number? ")
    num1 = get_int()

    print("What's the second number? ")
    num2 = get_int()

    print("What operation do you want to perform? ")
    operation = get_operator()

    match operation:
        case "+":
            output = num1 + num2
        case "-":
            output = num1 - num2
        case "*":
            output = num1 * num2
        case "/":
            output = num1 // num2

    print(f"{num1} {operation} {num2} = {output}")
    print("Go again? Enter \"q\" to quit.")
    if user_prompt() == "q":
        break

print("~~~~~~~~~~Thank you for running calculator.py!~~~~~~~~~~")