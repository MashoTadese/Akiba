
print("==============================")
print("          FIZZBUZZ")
print("==============================")

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for number in range(start, end + 1):

    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

    elif number % 3 == 0:
        print("Fizz")

    elif number % 5 == 0:
        print("Buzz")

    else:
        print(number)

print("==============================")
