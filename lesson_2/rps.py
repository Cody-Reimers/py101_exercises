import json
import random

LANGUAGE = "en"

with open("rps_messages.json", "r") as file:
    SOURCE_TEXT = json.load(file)[LANGUAGE]

VALID_CHOICES = SOURCE_TEXT["choices"]
QUIT = VALID_CHOICES[0]
MOVE_CHOICES = VALID_CHOICES[1:]

def get_user_choice():
    choice = ""

    while choice not in VALID_CHOICES:
        print("\n    " + SOURCE_TEXT["choices_intro"], ", ".join(MOVE_CHOICES))
        print("    " + SOURCE_TEXT["quit_intro"], f"\"{QUIT}\"\n")

        choice = input("===> ")

    return choice

def display_end_state(user, computer):
    messages = SOURCE_TEXT["end_states"]

    offset = find_index_offset(computer, user, MOVE_CHOICES)

    match offset % len(MOVE_CHOICES):
        case 2:
            print("    " + messages["victory"])
        case 1:
            print("    " + messages["loss"])
        case 0:
            print("    " + messages["tie"])

def find_index_offset(element1, element2, source):
    # Error shouldn't be possible based off this program alone,
    # but checking for ValueError makes the code more reusable.
    try:
        num1 = source.index(element1)
        num2 = source.index(element2)
    except ValueError:
        print("\n    " + SOURCE_TEXT["not_in_list"])

    return num1 - num2

print("\n    ~~~~" + SOURCE_TEXT["welcome"] + "~~~~\n")

while True:
    user_choice = get_user_choice()
    computer_choice = random.choice(MOVE_CHOICES)

    if user_choice == QUIT:
        print("\n    " + SOURCE_TEXT["quitting"] + "")
        break

    print("\n    " + SOURCE_TEXT["your_move"], user_choice + ",",
        SOURCE_TEXT["computer_move"], computer_choice + ".")

    display_end_state(user_choice, computer_choice)

print("    ~~~~" + SOURCE_TEXT["thanks"] + "~~~~\n")
