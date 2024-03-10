import json

def error_message():
    message = ""
    message += MESSAGES["error1"] + MESSAGES["error2"] + MESSAGES["error3"]
    message += f"{VALID_OPERATORS};\n" + MESSAGES["error4"]
    return message

def valid_float(number_str):
    try:
        float(number_str)
    except ValueError:
        return False

    return True

def proper_grouping(particle_type):
    if not types:
        if particle_type == "number":
            return True

    last = types[-1]

    match particle_type:
        case "operator":
            if last == "operator":
                return False
        case "number":
            if last in ("integer", "float"):
                return False

    return True

def calculate():
    if len(equation) == 1:
        return simple_eval(types[0])
    if types[-1] == "operator":
        return simple_eval("operator")

    operations_remaining = types.count("operator")

    while operations_remaining:
        if "**" in equation:
            index = find_first(["**"])
            mutate_lists(index, "**")
            operations_remaining -= 1
            continue

        if ("*" in equation) or ("/" in equation) or ("//" in equation):
            index = find_first(["*", "/", "//"])
            if equation[index] == "*":
                mutate_lists(index, "*")
            elif equation[index] == "/":
                mutate_lists(index, "/")
            elif equation[index] == "//":
                mutate_lists(index, "//")
            operations_remaining -= 1
            continue

        if ("+" in equation) or ("-" in equation):
            index = find_first(["+", "-"])
            if equation[index] == "+":
                mutate_lists(index, "+")
            elif equation[index] == "-":
                mutate_lists(index, "-")
            operations_remaining -= 1
            continue

    return equation[0]

def simple_eval(identity):
    match identity:
        case "integer":
            return int(equation[0])
        case "float":
            return float(equation[0])
        case _:
            return "ERROR/INVALID"

def find_first(targets):
    for element in equation[1::2]:
        for target in targets:
            if element == target:
                return equation.index(target)

    return None

def mutate_lists(i, op):
    num1 = get_num(equation[i - 1], types[i - 1])
    num2 = get_num(equation[i + 1], types[i + 1])

    match op:
        case "**":
            equation[i - 1] = num1 ** num2
        case "*":
            equation[i - 1] = num1 * num2
        case "/":
            equation[i - 1] = num1 / num2
        case "//":
            equation[i - 1] = num1 // num2
        case "+":
            equation[i - 1] = num1 + num2
        case "-":
            equation[i - 1] = num1 - num2

    if isinstance(equation[i - 1], int):
        types[i - 1] = "integer"
    elif isinstance(equation[i - 1], float):
        types[i - 1] = "float"

    del equation[i:i + 2]
    del types[i:i + 2]

def get_num(num_str, data_type):
    match data_type:
        case "integer":
            return int(num_str)
        case "float":
            return float(num_str)

VALID_OPERATORS = ["+", "-", "*", "/", "//", "**"]

with open("float_calculator.json", "r") as file:
    MESSAGES = json.load(file)

print(MESSAGES["intro1"], MESSAGES["intro2"], MESSAGES["intro3"],
    MESSAGES["intro4"], MESSAGES["intro5"], MESSAGES["intro6"],
    MESSAGES["intro7"], MESSAGES["intro8"], MESSAGES["intro9"],
    MESSAGES["intro10"], MESSAGES["intro11"], MESSAGES["intro12"])

equation = []
types = []

while True:
    if equation:
        print("".join(equation))

    next_particle = input("===> ")

    if next_particle == "quit":
        break

    if next_particle == "delete":
        try:
            del equation[-1]
            del types[-1]
        except IndexError:
            print(MESSAGES["empty_list_error"])
        continue

    if next_particle == "complete":
        if equation:
            print("".join(equation) + f" = {calculate()}")
            equation.clear()
            types.clear()
            print(MESSAGES["begin_again"])
        else:
            print(MESSAGES["empty_list_error"])
        continue

    if next_particle.isnumeric():
        if not proper_grouping("number"):
            print(error_message())
        else:
            equation.append(next_particle)
            types.append("integer")
        continue

    if valid_float(next_particle):
        if not proper_grouping("number"):
            print(error_message())
        else:
            equation.append(next_particle)
            types.append("float")
        continue

    if next_particle in VALID_OPERATORS:
        if not proper_grouping("operator"):
            print(error_message())
        else:
            equation.append(next_particle)
            types.append("operator")
        continue

#   If all else fails....
    print(error_message())

print(MESSAGES["farewell"])