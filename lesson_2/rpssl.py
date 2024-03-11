import json
import random

LANGUAGE = "en"

with open("rps_messages.json", "r") as file:
    SOURCE_TEXT = json.load(file)[LANGUAGE]

VALID_CHOICES = SOURCE_TEXT["choices"]
QUIT = VALID_CHOICES[0]
MOVE_CHOICES = VALID_CHOICES[1:]

def generate_unique_abbreviations(collection):
    abbreviations = generate_abbreviations(collection)

    is_unique = check_for_uniqueness(abbreviations)

    while False in is_unique:
        where_false = is_unique.index(False)
        identical_element = abbreviations[where_false]

        while identical_element in abbreviations:
            where_false = abbreviations.index(identical_element)

            abbreviations[where_false] = generate_abbreviations(
                [collection[where_false]], (len(identical_element) + 1))[0]

        is_unique = check_for_uniqueness(abbreviations)

    while "" in abbreviations:
        abbreviations.remove("")

    return abbreviations

def generate_abbreviations(collection, abv_len=1):
    abbreviations = []

    for element in collection:
        try:
            abbreviations.append(element[0:abv_len])
        except IndexError:
            abbreviations.append("")

    return abbreviations

def check_for_uniqueness(collection):
    is_unique = []

    for element in collection:
        if (not element) or collection.count(element) == 1:
            is_unique.append(True)
        else:
            is_unique.append(False)

    return is_unique

def determine_longest(collection):
    longest = 0

    for element in collection:
        longest = max(longest, len(element))

    return longest

ABBREVIATIONS = generate_unique_abbreviations(VALID_CHOICES)
GREATEST_LENGTH = determine_longest(VALID_CHOICES)
#   Used as a simple guard against silly inputs

def get_user_choice():
    choice = ""

    while ((not starts_with_abbreviation(choice)) and
        (choice not in VALID_CHOICES) and (len(choice) <= GREATEST_LENGTH)):
        if choice:
            print("\n    ".join(SOURCE_TEXT["error_guide"]) + "\n")
        else:
            print("\n    " + SOURCE_TEXT["choices_intro"],
                ", ".join(MOVE_CHOICES))
            print("    " + SOURCE_TEXT["quit_intro"], f"\"{QUIT}\"\n")

        choice = input("===> ").strip()

    abbreviation = starts_with_abbreviation(choice)

    if abbreviation:
        choice = expand_abbreviation(abbreviation)

    return choice

def starts_with_abbreviation(string):
    for abbreviation in ABBREVIATIONS:
        if string.lower().startswith(abbreviation):
            return abbreviation

    return ""

def expand_abbreviation(abbreviation):
    for choice in VALID_CHOICES:
        if choice.startswith(abbreviation):
            return choice

    return "quit"

def update_game_history(user, computer):
    offset = find_index_offset(computer, user, MOVE_CHOICES)

    match offset % len(MOVE_CHOICES):
        case 1:
            game_history.append("computer")
        case 2:
            game_history.append("user")
        case 3:
            game_history.append("computer")
        case 4:
            game_history.append("user")

def display_end_state(user, computer):
    messages = SOURCE_TEXT["end_states"]

    offset = find_index_offset(computer, user, MOVE_CHOICES)

    match offset % len(MOVE_CHOICES):
        case 0:
            print("    " + messages["tie"])
        case 1:
            print("    " + messages["loss"])
        case 2:
            print("    " + messages["victory"])
        case 3:
            print("    " + messages["loss"])
        case 4:
            print("    " + messages["victory"])

    if game_history.count("computer") == 3:
        print("    " + messages["set_loss"])
        game_history.clear()
    elif game_history.count("user") == 3:
        print("    " + messages["set_victory"])
        game_history.clear()

def find_index_offset(element1, element2, source):
    # Error shouldn't be possible based off this program alone,
    # but checking for ValueError makes the code more reusable.
    try:
        num1 = source.index(element1)
        num2 = source.index(element2)
    except ValueError:
        print("\n    " + SOURCE_TEXT["not_in_list"])

    return num1 - num2

def gross_add_choice_space(times):
    for _ in range(times):
        for move in MOVE_CHOICES:
            if computer_choice_space.count(move) < 24:
                computer_choice_space.append(move)

#   The number of times moves are repeated in the computer_choice_space,
#   and the number of additions and subtractions from the
#   computer_choice_space are arbitrary, based on what looks good to me.

def decide_adjustment(user, computer):
    offset = find_index_offset(computer, user, MOVE_CHOICES)

    match offset % len(MOVE_CHOICES):
        case 0:
            gross_add_choice_space(1)
            adjust_choice_space(computer, -2)
        case 1:
            adjust_choice_space(computer, 3)
        case 2:
            adjust_choice_space(computer, -3)
        case 3:
            adjust_choice_space(computer, 3)
        case 4:
            adjust_choice_space(computer, -3)

def adjust_choice_space(move, times):
    if times > 0:
        for _ in range(times):
            if computer_choice_space.count(move) < 24:
                computer_choice_space.append(move)
            else:
                break
    elif times < 0:
        for _ in range(-times):
            if computer_choice_space.count(move) > 1:
                computer_choice_space.remove(move)
            else:
                break

#   MAIN BODY

print("\n    ~~~~" + SOURCE_TEXT["welcome"] + "~~~~\n")

game_history = []

computer_choice_space = []
gross_add_choice_space(12)

while True:
    user_choice = get_user_choice()
    computer_choice = random.choice(computer_choice_space)

    if user_choice == QUIT:
        print("\n    " + SOURCE_TEXT["quitting"] + "")
        break

    print("\n    " + SOURCE_TEXT["your_move"], user_choice + ",",
        SOURCE_TEXT["computer_move"], computer_choice + ".")

    update_game_history(user_choice, computer_choice)
    display_end_state(user_choice, computer_choice)
    decide_adjustment(user_choice, computer_choice)

print("    ~~~~" + SOURCE_TEXT["thanks"] + "~~~~\n")
