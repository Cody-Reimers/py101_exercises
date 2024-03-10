def collect_valid_float(message):
    while True:
        try:
            number = float(input(f"{message} ===> "))
            if number <= 0:
                raise ValueError()
            else:
                return number
        except ValueError:
            print("\n    That input won't work.\n")


print("""
    This program will help you calculate the monthly cost
    of a mortgage or other loan, to do so you'll need to
    provide it a couple of numbers. The loan amount should
    be in the format of "dollars.cents"; the APR should
    be provided as a normal decimal numbers, like an APR
    of "3.5"%; and duration should be provided as a
    decimal representation of the number of years.
"""
)

principal = collect_valid_float("What is the loan amount?")
interest = collect_valid_float("What is the loan APR?") / 1200
months = collect_valid_float("How long is the loan for?") * 12

print(
"""
                                  /           interest          \\
    Monthly payment = principal * |-----------------------------|
                                  \\1 - (1 + interest)^(-months))/
"""
)

print(f"\n    Monthly payment = {principal} * ",
    f"({interest} / (1 - (1 + {interest}) ** {-months}))\n")

monthly_payment = principal * (interest / (1 - (1 + interest) ** -months))

print(f"Your monthly payment is ${float(int(monthly_payment * 100) / 100)}")