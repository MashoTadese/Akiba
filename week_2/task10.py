
print("==============================")
print("=======NUMBER ANALYZER=======")
print("==============================")

total = 0
even_count = 0
odd_count = 0

for count in range(1, 11):
    number = int(input("Enter number " + str(count) + ": "))

    if count == 1:
        largest = number
        smallest = number
    else:
        if number > largest:
            largest = number

        if number < smallest:
            smallest = number

    total = total + number

    if number % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

average = total / 10

print()
print("========== RESULTS ==========")
print("Largest number:", largest)
print("Smallest number:", smallest)
print("Total sum:", total)
print("Average:", average)
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
print("==============================")
