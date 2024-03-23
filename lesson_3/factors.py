def factors(number):
    if number < 0:
        divisor = -number
    elif number > 0:
        divisor = number

    result = []

    while divisor > min(0, number):
        if number % divisor == 0:
            result.append(number // divisor)

        divisor -= 1

    return result

print(factors(int(input("What number do you want to factorize? ===> "))))
