
print("==============================")
print("=======ATM PIN SYSTEM=====")
print("==============================")

correct_pin = "2143"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    pin = input("Enter your PIN: ")
    attempts = attempts + 1

    if pin == correct_pin:
        print("PIN verified successfully!")
        print("Welcome to your account.")
        break

    else:
        remaining = max_attempts - attempts
        print("Incorrect PIN.")

        if remaining > 0:
            print("Attempts remaining: " ,remaining)
        else:
            print("Your ATM card is locked!")
            
print("==============================")
