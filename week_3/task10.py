
def add_expense(expenses, description, category, amount):
    if amount < 0:
        print("Error: Expense amount cannot be negative.")
        return

    expense = {
        "description": description,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully!")


def calculate_total_expenses(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total


def calculate_spending_by_category(expenses):
    category_totals = {}

    for expense in expenses:
        category = expense["category"]

        if category not in category_totals:
            category_totals[category] = 0

        category_totals[category] += expense["amount"]

    return category_totals


def find_largest_expense(expenses):
    if len(expenses) == 0:
        return None

    largest = expenses[0]

    for expense in expenses:
        if expense["amount"] > largest["amount"]:
            largest = expense

    return largest


def find_expenses_above_threshold(expenses, threshold):
    matching_expenses = []

    for expense in expenses:
        if expense["amount"] > threshold:
            matching_expenses.append(expense)

    return matching_expenses


def calculate_category_percentages(category_totals, total):
    percentages = {}

    for category, amount in category_totals.items():
        if total > 0:
            percentages[category] = (amount / total) * 100
        else:
            percentages[category] = 0

    return percentages


def find_highest_spending_category(category_totals):
    if len(category_totals) == 0:
        return None

    highest_category = None
    highest_amount = -1

    for category, amount in category_totals.items():
        if amount > highest_amount:
            highest_amount = amount
            highest_category = category

    return highest_category, highest_amount


def generate_spending_report(expenses, threshold):
    if len(expenses) == 0:
        print("\nNo expenses to analyze.")
        return

    total = calculate_total_expenses(expenses)
    category_totals = calculate_spending_by_category(expenses)
    percentages = calculate_category_percentages(category_totals, total)
    largest = find_largest_expense(expenses)
    highest_category = find_highest_spending_category(category_totals)
    expensive_items = find_expenses_above_threshold(expenses, threshold)

    print("\n========== SPENDING REPORT ==========")

    print("\nAll Expenses:")
    for expense in expenses:
        print(
            expense["description"], "|",
            expense["category"], "|",
            expense["amount"], "Birr"
        )

    print("\nTotal Expenses:", total, "Birr")

    print("\nSpending by Category:")
    for category, amount in category_totals.items():
        print(
            category + ":",
            amount, "Birr",
            "(" + str(round(percentages[category], 2)) + "%)"
        )

    print("\nLargest Expense:")
    print(
        largest["description"], "-",
        largest["amount"], "Birr",
        "(" + largest["category"] + ")"
    )

    print("\nExpenses Above", threshold, "Birr:")
    if len(expensive_items) == 0:
        print("No expenses above the threshold.")
    else:
        for expense in expensive_items:
            print(
                expense["description"], "-",
                expense["amount"], "Birr"
            )

    print("\nHighest Spending Category:")
    print(
        highest_category[0], "-",
        highest_category[1], "Birr"
    )

    print("=====================================")


def main():
    expenses = [
        {"description": "Lunch", "category": "Food", "amount": 180},
        {"description": "Taxi", "category": "Transport", "amount": 120},
        {"description": "Groceries", "category": "Food", "amount": 450},
        {"description": "Internet", "category": "Bills", "amount": 300}
    ]

    print("===== EXPENSE ANALYZER =====")
    print("1. Add an expense")
    print("2. Generate spending report")

    choice = input("Choose an option (1 or 2): ").strip()

    if choice == "1":
        description = input("Enter expense description: ").strip()
        category = input("Enter expense category: ").strip()

        try:
            amount = float(input("Enter expense amount in Birr: "))

            if description == "" or category == "":
                print("Description and category cannot be empty.")
            elif amount < 0:
                print("Expense amount cannot be negative.")
            else:
                add_expense(expenses, description, category, amount)
                threshold = float(
                    input("Enter spending threshold in Birr: ")
                )

                if threshold < 0:
                    print("Threshold cannot be negative.")
                else:
                    generate_spending_report(expenses, threshold)

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "2":
        try:
            threshold = float(
                input("Enter spending threshold in Birr: ")
            )

            if threshold < 0:
                print("Threshold cannot be negative.")
            else:
                generate_spending_report(expenses, threshold)

        except ValueError:
            print("Please enter a valid number.")

    else:
        print("Invalid choice. Please select 1 or 2.")


main()
