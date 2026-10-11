
print("==============================")
print("======NUMBER GUESSING GAME======")
print("==============================")

secret_number = 15
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    guess = int(input("Guess a number (1-20): "))
    attempts = attempts + 1

    if guess == secret_number:
        print("Congratulations!")
        print("You guessed the number in" ,attempts, "attempts.")
        break

    elif guess < secret_number:
        print("Too low! Try a higher number.")

    else:
        print("Too high! Try a lower number.")

if attempts == max_attempts and guess != secret_number:
    print("Game Over!")
    print("The secret number was" ,secret_number)

print("==============================")
