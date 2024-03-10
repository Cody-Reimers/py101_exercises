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

print("""
    This program can handle integer numbers and decimal numbers.
    Other than numbers, this program supports the following symbols:
    "+" (addition), "-" (subtraction), "*" (multiplication),
    "/" (decimal divison), "//" (integer divison), and "**" (exponents).
    
    Each time the calculator asks you for input, you must:
    enter only a number; enter a single valid operation symbol;
    or input "delete", "quit", or "complete".
    
    Enter "delete" to remove the last number or operation symbol;
    enter "quit" to let the calculator know you are done;
    enter "complete" to run a calculation.
    
    The calculator will print what the calculation currently
    looks like as you go, to improve interactivity.
"""
)

VALID_OPERATORS = ["+", "-", "*", "/", "//", "**"]

ERROR_MESSAGE = ("\n    Your input was not validated. Make sure you\n"
    "    use proper grouping rules, and that your input is:\n"
    "    a number (integers like \"42\" or decimals like \"3.14159\");\n"
    f"    an operator {VALID_OPERATORS};\n"
    "    or \"delete\", \"quit\", or \"complete\"\n")

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
            print("You haven't entered anything yet!")
        continue

    if next_particle == "complete":
        if equation:
            print("".join(equation) + f" = {calculate()}")
            equation.clear()
            types.clear()
            print("Beginning work on a new calculation...")
        else:
            print("You haven't entered anything yet!")
        continue

    if next_particle.isnumeric():
        if not proper_grouping("number"):
            print(ERROR_MESSAGE)
        else:
            equation.append(next_particle)
            types.append("integer")
        continue

    if valid_float(next_particle):
        if not proper_grouping("number"):
            print(ERROR_MESSAGE)
        else:
            equation.append(next_particle)
            types.append("float")
        continue

    if next_particle in VALID_OPERATORS:
        if not proper_grouping("operator"):
            print(ERROR_MESSAGE)
        else:
            equation.append(next_particle)
            types.append("operator")
        continue

#   If all else fails....
    print(ERROR_MESSAGE)

print("\nThank you for running float_calculator.py\n")