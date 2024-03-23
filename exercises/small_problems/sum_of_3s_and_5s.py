def print_system(message, start_with_blank_line=True,
        end_with_blank_line=True):
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
    print_system("What's the number you want to sum up to?")

    while True:
        number_string = get_user_input()

        try:
            user_number = int(number_string)
            if user_number < 1:
                raise ValueError()
        except ValueError:
            print_system("Must enter a positive non-zero integer.")
            continue

        return user_number

def get_quit():
    print_system("Do you want to quit the calculator: y/n?")

    while True:
        choice = get_user_input().lower()

        if choice in ("y", "n"):
            return choice

        print_system("Must choose \"yes\" or \"no\":" +
                " enter \"y\" or \"n\"")

def sum_3s_and_5s_up_to(target):
    multiples_of_3 = range(3, target + 1, 3)
    multiples_of_5 = range(5, target + 1, 5)
    result = 0

    for multiple in multiples_of_3:
        result += multiple

    for multiple in multiples_of_5:
        if multiple not in multiples_of_3:
            result += multiple

    return result

def main():
    user_number = get_user_number()

    result = sum_3s_and_5s_up_to(user_number)

    print_system(("The sum of all multiples of 3 and 5 up " +
            f"to the target number is: {result}"))

print_status(["Welcome to the sum of multiples of 3 and 5 calculator!",
        "This program will sum up each unique number that is a",
        "multiple of 3 or 5, up to a target number you provide."])

keep_going = True

while keep_going:
    main()

    quit_choice = get_quit()

    if quit_choice == "y":
        keep_going = False

print_status(["Thanks for using this calculator!",
        "I hope it helped you; have a good day!"])
