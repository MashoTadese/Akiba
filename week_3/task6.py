
# Inventory storage
inventory = {}


# 1. Add a new product
def add_product(name, price, stock):
    name = name.strip()

    if name == "":
        print("Error: Product name cannot be empty.")
        return False

    if name.lower() in inventory:
        print("Error: Product already exists.")
        return False

    if price < 0:
        print("Error: Price cannot be negative.")
        return False

    if stock < 0:
        print("Error: Stock cannot be negative.")
        return False

    inventory[name.lower()] = {
        "name": name,
        "price": price,
        "stock": stock
    }

    print("Product added successfully!")
    return True


# 2. Search for a product
def search_product(name):
    name = name.strip().lower()

    if name in inventory:
        return inventory[name]

    return None


# 3. Update a product's price
def update_price(name, new_price):
    product = search_product(name)

    if product is None:
        print("Error: Product not found.")
        return False

    if new_price < 0:
        print("Error: Price cannot be negative.")
        return False

    product["price"] = new_price

    print("Price updated successfully!")
    return True


# 4. Increase stock
def increase_stock(name, quantity):
    product = search_product(name)

    if product is None:
        print("Error: Product not found.")
        return False

    if quantity <= 0:
        print("Error: Quantity must be positive.")
        return False

    product["stock"] += quantity

    print("Stock increased successfully!")
    return True


# 5. Sell a product
def sell_product(name, quantity):
    product = search_product(name)

    if product is None:
        print("Error: Product not found.")
        return False

    if quantity <= 0:
        print("Error: Quantity must be positive.")
        return False

    if quantity > product["stock"]:
        print("Error: Not enough stock available.")
        return False

    product["stock"] -= quantity

    total_price = product["price"] * quantity

    print("Sale successful!")
    print("Product:", product["name"])
    print("Quantity sold:", quantity)
    print("Total sale amount:", total_price)
    print("Remaining stock:", product["stock"])

    return True


# 6. Calculate total inventory value
def total_inventory_value():
    total = 0

    for product in inventory.values():
        total += product["price"] * product["stock"]

    return total


# 7. Generate a low-stock report
def low_stock_report(threshold=5):
    low_stock = []

    for product in inventory.values():
        if product["stock"] < threshold:
            low_stock.append(product)

    return low_stock


# 8. Display all products
def display_inventory():
    if len(inventory) == 0:
        print("Inventory is empty.")
        return

    print("\n===== INVENTORY =====")

    for product in inventory.values():
        print(
            "Name:", product["name"],
            "| Price:", product["price"],
            "| Stock:", product["stock"]
        )

    print("Total inventory value:", total_inventory_value())


# 9. Main program
while True:
    print("\n===== INVENTORY MENU =====")
    print("1. Add Product")
    print("2. Search Product")
    print("3. Update Price")
    print("4. Increase Stock")
    print("5. Sell Product")
    print("6. Total Inventory Value")
    print("7. Low-Stock Report")
    print("8. Display Inventory")
    print("9. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        stock = int(input("Enter stock quantity: "))
        add_product(name, price, stock)

    elif choice == "2":
        name = input("Enter product name to search: ")
        product = search_product(name)

        if product is not None:
            print(product)
        else:
            print("Product not found.")

    elif choice == "3":
        name = input("Enter product name: ")
        price = float(input("Enter new price: "))
        update_price(name, price)

    elif choice == "4":
        name = input("Enter product name: ")
        quantity = int(input("Enter quantity to add: "))
        increase_stock(name, quantity)

    elif choice == "5":
        name = input("Enter product name: ")
        quantity = int(input("Enter quantity to sell: "))
        sell_product(name, quantity)

    elif choice == "6":
        print("Total inventory value:", total_inventory_value())

    elif choice == "7":
        threshold = int(
            input("Enter low-stock threshold (default is 5): ") or 5
        )

        products = low_stock_report(threshold)

        if len(products) == 0:
            print("No low-stock products.")
        else:
            print("\n===== LOW-STOCK REPORT =====")

            for product in products:
                print(
                    product["name"],
                    "- Remaining stock:",
                    product["stock"]
                )

    elif choice == "8":
        display_inventory()

    elif choice == "9":
        print("Inventory program closed.")
        break

    else:
        print("Invalid choice. Try again.")
