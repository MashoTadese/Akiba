
# Configurable settings
opening_balance = 1000
daily_withdrawal_limit = 2000


# Store successful transactions
transactions = []


# Track total deposited and withdrawn
total_deposited = 0
total_withdrawn = 0


# Track withdrawals made today
daily_withdrawn = 0


# 1. Record a successful transaction
def record_transaction(transaction_type, amount, balance):
    transaction = {
        "type": transaction_type,
        "amount": amount,
        "balance_after": balance
    }

    transactions.append(transaction)


# 2. Deposit money
def deposit(amount):
    global opening_balance, total_deposited

    if amount <= 0:
        print("Error: Deposit amount must be positive.")
        return False

    opening_balance += amount
    total_deposited += amount

    record_transaction("deposit", amount, opening_balance)

    print("Deposit successful!")
    print("Current balance:", opening_balance)

    return True


# 3. Withdraw money
def withdraw(amount):
    global opening_balance, total_withdrawn, daily_withdrawn

    if amount <= 0:
        print("Error: Withdrawal amount must be positive.")
        return False

    if amount > opening_balance:
        print("Error: Insufficient balance.")
        return False

    remaining_limit = daily_withdrawal_limit - daily_withdrawn

    if amount > remaining_limit:
        print("Error: Daily withdrawal limit exceeded.")
        print("Remaining withdrawal limit:", remaining_limit)
        return False

    opening_balance -= amount
    total_withdrawn += amount
    daily_withdrawn += amount

    record_transaction("withdrawal", amount, opening_balance)

    print("Withdrawal successful!")
    print("Current balance:", opening_balance)

    return True


# 4. Check current balance
def check_balance():
    return opening_balance


# 5. Generate transaction summary
def transaction_summary():
    print("\n===== BANK TRANSACTION SUMMARY =====")
    print("Opening balance:", initial_balance)
    print("Total deposited:", total_deposited)
    print("Total withdrawn:", total_withdrawn)
    print("Daily withdrawal limit:", daily_withdrawal_limit)
    print("Withdrawn today:", daily_withdrawn)
    print("Remaining daily limit:",
          daily_withdrawal_limit - daily_withdrawn)
    print("Final balance:", check_balance())

    print("\nTransaction History:")

    if len(transactions) == 0:
        print("No successful transactions.")
    else:
        for transaction in transactions:
            print(
                "Type:", transaction["type"],
                "| Amount:", transaction["amount"],
                "| Balance after:", transaction["balance_after"]
            )


# Save the opening balance
initial_balance = opening_balance


# 6. Main program
while True:
    print("\n===== BANK MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction Summary")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        withdraw(amount)

    elif choice == "3":
        print("Current balance:", check_balance())

    elif choice == "4":
        transaction_summary()

    elif choice == "5":
        print("Thank you for using our banking program!")
        transaction_summary()
        break

    else:
        print("Invalid choice. Please try again.")
