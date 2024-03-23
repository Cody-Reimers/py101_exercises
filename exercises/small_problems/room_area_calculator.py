import math

SQUARE_METERS_TO_SQUARE_FEET = 10.7639

def get_valid_float():
    number = 0.0

    while True:
        try:
            number = float(input("===> ").strip())
            if math.isnan(number) or math.isinf(number):
                raise ValueError()

            break
        except ValueError:
            print("\n    Please provide an integer or decimal number.\n")

    return number

def get_valid_choice():
    print("\n    Do you want the measurement in square feet or meters?")
    print("    Enter \"feet\" or \"meters\" to choose.\n")

    while True:

        unit_type = input("===> ").strip()

        if unit_type in ("feet", "meters"):
            return unit_type

        print("\n    Please enter either \"feet\" or \"meters\".\n")

def calculate_areas(length, width):
    answer = {
        "meters": length * width,
        "feet": length * width * SQUARE_METERS_TO_SQUARE_FEET
    }
    return answer

print("\n    Please give me the length of the room in meters.\n")
room_length = int(get_valid_float())

print("\n    Please give me the width of the room in meters.\n")
room_width = int(get_valid_float())

areas = calculate_areas(room_length, room_width)

choice = get_valid_choice()

print(f"\n    The area of the room is {areas[choice]:.2f} in {choice}.")