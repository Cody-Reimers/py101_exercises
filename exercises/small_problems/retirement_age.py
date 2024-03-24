from datetime import date

def print_system(message, start_with_blank_line=True,
        end_with_blank_line=True):
    if start_with_blank_line:
        print("")

    print("    " + message)

    if end_with_blank_line:
        print("")

def get_user_input():
    return input("===> ").strip()

def get_age():
    while True:
        age = get_user_input()

        try:
            age = int(age)
        except ValueError:
            print_system("Need an integer for an age.")
            continue

        return age

def main():
    print_system("What is your current age?")
    age = get_age()

    print_system("At what age would you like to retire?")
    retirement_age = get_age()

    age_difference = retirement_age - age

    the_present = date.today()

    print_system((f"It's currently {the_present.year}. " +
            "Your current plan would be to retire in " +
            f"{the_present.year + age_difference}."), True, False)
    print_system((f"You have only {age_difference} years " +
            "of work left to go!"), False)

main()
