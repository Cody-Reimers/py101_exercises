def print_system(message, start_with_blank_line=False,
        end_with_blank_line=False):
    if start_with_blank_line:
        print("")

    print("    " + message)

    if end_with_blank_line:
        print("")

def print_status(text):
    if isinstance(text, str):
        text = [text]

    print("")
    print("+" + "-" * 77 + "+")
    for line in text:
        print("|" + line.center(77, ".") + "|")
    print("+" + "-" * 77 + "+")
    print("")

def get_user_input():
    return input("===> ").strip()

def get_user_number():
    print_system("Provide the target number you want the calculator" +
            " to add or multiply up to for you.", True, True)

    while True:
        number_string = get_user_input()

        try:
            user_number = int(number_string)
            if user_number < 1:
                raise ValueError()
        except ValueError:
            print_system("Must enter a positive non-zero integer.", True, True)
            continue

        return user_number

def get_user_choice():
    print_system("Choose whether to get the sum or product" +
            " up to your target number.", True, True)

    while True:
        choice = get_user_input().lower()

        if choice in ("s", "p"):
            return choice

        print_system("Must choose to either calculate a \"sum\"" +
                " or \"product\": enter \"s\" or \"p\"", True, True)

def get_quit():
    print_system("Do you want to quit the calculato: y/n?", True, True)

    while True:
        choice = get_user_input().lower()

        if choice in ("y", "n"):
            return choice

        print_system("Much choose \"yes\" or \"no\":" +
                " enter \"y\" or \"n\"", False, True)

def sum_up_to(target):
    numbers_up_to_target = range(1, target + 1)
    result = 0

    for number in numbers_up_to_target:
        result += number

    return result

def product_up_to(target):
    numbers_up_to_target = range(1, target + 1)
    result = 1

    for number in numbers_up_to_target:
        result *= number

    return result

def main():
    user_number = get_user_number()
    choice = get_user_choice()

    if choice == "p":
        result = product_up_to(user_number)
    if choice == "s":
        result = sum_up_to(user_number)

    print_system(f"The operation result is: {result}", True, True)

print_status(["Welcome to the Mass Integer Operation Calculator!",
        "This program can help you find the sum or product",
        "of all integers from 1 up to a target number you",
        "specify. You\'ll be prompted to enter a number",
        "and then choose to either get the sum or product",
        "by entering \"s\" or \"p\"."])

keep_going = True

while keep_going:
    main()

    quit_choice = get_quit()

    if quit_choice == "y":
        keep_going = False

print_status(["Thanks for using the Mass Integer Operation Calculator!",
        "I hope it has served you well, and wish you a good day!"])
