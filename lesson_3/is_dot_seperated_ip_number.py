def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")

    if len(dot_separated_words) != 4:
        return False

    for word in dot_separated_words:
        if not is_an_ip_number(word):
            return False

    return True

def is_an_ip_number(str):
    if str.isdigit():
        number = int(str)
        return 0 <= number <= 255

    return False