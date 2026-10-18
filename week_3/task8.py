
# 1. Validate units consumed
def validate_units(units):
    return units >= 0


# 2. Calculate the charge for each tier
def calculate_tier_charges(units):
    first_tier = 0
    second_tier = 0
    third_tier = 0

    if units > 0:
        if units <= 50:
            first_tier = units * 0.50
        else:
            first_tier = 50 * 0.50

            if units <= 150:
                second_tier = (units - 50) * 0.75
            else:
                second_tier = 100 * 0.75
                third_tier = (units - 150) * 1.20

    return {
        "first_tier": first_tier,
        "second_tier": second_tier,
        "third_tier": third_tier
    }


# 3. Calculate the total bill
def calculate_total_bill(units, service_fee=0):
    if not validate_units(units):
        raise ValueError("Units consumed cannot be negative.")

    if service_fee < 0:
        raise ValueError("Service fee cannot be negative.")

    charges = calculate_tier_charges(units)

    energy_charge = (
        charges["first_tier"]
        + charges["second_tier"]
        + charges["third_tier"]
    )

    total = energy_charge + service_fee

    return total


# 4. Generate a billing summary
def generate_billing_summary(units, service_fee=0):
    if not validate_units(units):
        raise ValueError("Units consumed cannot be negative.")

    if service_fee < 0:
        raise ValueError("Service fee cannot be negative.")

    charges = calculate_tier_charges(units)
    energy_charge = (
        charges["first_tier"]
        + charges["second_tier"]
        + charges["third_tier"]
    )

    total = calculate_total_bill(units, service_fee)

    summary = {
        "Units consumed": units,
        "First 50 units charge": charges["first_tier"],
        "Next 100 units charge": charges["second_tier"],
        "Above 150 units charge": charges["third_tier"],
        "Energy charge": energy_charge,
        "Service fee": service_fee,
        "Total bill": total
    }

    return summary


# 5. Main program
try:
    units = float(input("Enter electricity units consumed: "))
    service_fee = float(
        input("Enter service fee (0 if none): ") or 0
    )

    summary = generate_billing_summary(units, service_fee)

    print("\n===== ELECTRICITY BILL SUMMARY =====")

    for item, amount in summary.items():
        print(item + ":", round(amount, 2), "Birr")

except ValueError as error:
    print("Error:", error)
