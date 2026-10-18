
def is_prime(number):
    if number < 2:
        return False

    divisor = 2

    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1

    return True


def get_divisors(number):
    # Divisors are defined here for positive integers only.
    if number <= 0:
        return []

    divisors = []

    for divisor in range(1, number + 1):
        if number % divisor == 0:
            divisors.append(divisor)

    return divisors


def sum_of_digits(number):
    number = abs(number)
    total = 0

    while number > 0:
        digit = number % 10
        total += digit
        number //= 10

    return total


def reverse_number(number):
    sign = -1 if number < 0 else 1
    number = abs(number)
    reversed_value = 0

    while number > 0:
        digit = number % 10
        reversed_value = reversed_value * 10 + digit
        number //= 10

    return sign * reversed_value


def analyze_number(number):
    if not isinstance(number, int) or isinstance(number, bool):
        raise TypeError("Please provide an integer.")

    if number % 2 == 0:
        parity = "Even"
    else:
        parity = "Odd"

    analysis = {
        "number": number,
        "parity": parity,
        "is_prime": is_prime(number),
        "sum_of_digits": sum_of_digits(number),
        "reversed_number": reverse_number(number),
        "divisors": get_divisors(number)
    }

    return analysis


# Test the program
result = analyze_number(123)

for key, value in result.items():
    print(key, ":", value)
