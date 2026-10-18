
def calculate_subtotal(items):
    subtotal = 0

    for item in items:
        if item["price"] < 0:
            raise ValueError("Price cannot be negative.")

        if item["quantity"] < 0:
            raise ValueError("Quantity cannot be negative.")

        subtotal = subtotal + item["price"] * item["quantity"]

    return subtotal


def calculate_discount(subtotal):
    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative.")

    if subtotal < 1000:
        discount = 0
    elif subtotal < 3000:
        discount = subtotal * 0.05
    else:
        discount = subtotal * 0.10

    return discount


def calculate_tax(amount, tax_rate):
    if amount < 0:
        raise ValueError("Amount cannot be negative.")

    if tax_rate < 0 or tax_rate > 100:
        raise ValueError("Tax rate must be between 0 and 100.")

    tax = amount * tax_rate / 100
    return tax


def generate_receipt(items, tax_rate):
    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal)

    discounted_amount = subtotal - discount
    tax = calculate_tax(discounted_amount, tax_rate)

    final_amount = discounted_amount + tax

    receipt = {
        "items": items,
        "subtotal": subtotal,
        "discount": discount,
        "tax": tax,
        "final_amount": final_amount
    }

    return receipt


# Main program
items = [
    {"name": "Notebook", "price": 80, "quantity": 3},
    {"name": "Pen", "price": 15, "quantity": 5}
]

tax_rate = 15

try:
    receipt = generate_receipt(items, tax_rate)

    print("==============================")
    print("       SHOPPING RECEIPT")
    print("==============================")

    for item in receipt["items"]:
        item_total = item["price"] * item["quantity"]

        print(item["name"])
        print("  Price:", item["price"], "Birr")
        print("  Quantity:", item["quantity"])
        print("  Total:", item_total, "Birr")

    print("------------------------------")
    print("Subtotal:", round(receipt["subtotal"], 2), "Birr")
    print("Discount:", round(receipt["discount"], 2), "Birr")
    print("Tax:", round(receipt["tax"], 2), "Birr")
    print("Final Amount:", round(receipt["final_amount"], 2), "Birr")
    print("==============================")

except ValueError as error:
    print("Error:", error)
