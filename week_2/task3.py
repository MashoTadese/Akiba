print("=========Prime number============")
number=int(input("Enter a number: "))
if number <= 1:
    print("The number is not a prime number.")
else:
    is_prime = True
# We only check up to the square root because
# if we find a bigger divisor, there is a smaller
# one that matches it, so we don't need to check all numbers.
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print("The number is a prime number.")
    else:
        print("The number is not a prime number.")