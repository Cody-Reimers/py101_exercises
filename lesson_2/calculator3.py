import json

def user_prompt():
    return input("==> ")

def get_int():
    integer = user_prompt()
    if not integer.isnumeric():
        print(MESSAGES["invalid_num"])
        integer = get_int()
    return int(integer)

def get_operator():
    operator = user_prompt()
    valid_operators = ["+", "-", "*", "/"]
    if operator not in valid_operators:
        print(MESSAGES["invalid_operation"])
        operator = get_operator()
    return operator

LANGUAGE = "en" # "en" for English, "es" for Spanish
with open("calculator_messages.json", "r") as file:
    MESSAGES = json.load(file)[LANGUAGE]

print(MESSAGES["welcome"])
print(MESSAGES["introduction_line1"] + MESSAGES["introduction_line2"] +
    MESSAGES["introduction_line3"] + MESSAGES["introduction_line4"])

while True:
    print(MESSAGES["request_num1"])
    num1 = get_int()

    print(MESSAGES["request_num2"])
    num2 = get_int()

    print(MESSAGES["request_operation"])
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
    print(MESSAGES["prompt_for_continue"])
    if user_prompt() == "q":
        break

print(MESSAGES["farewell"])