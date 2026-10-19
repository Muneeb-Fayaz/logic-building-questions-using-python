"""
Question 3: Electricity Bill Calculator
---------------------------------------
Slab-based billing (the more you use, the more each unit costs):

    First 100 units    -> Rs. 3 per unit
    Next 100 units     -> Rs. 5 per unit   (101 - 200)
    Next 100 units     -> Rs. 7 per unit   (201 - 300)
    Above 300 units    -> Rs. 10 per unit

Plus a fixed meter charge of Rs. 50.
"""


def calculate_bill(units):
    bill = 0

    if units <= 100:
        bill = units * 3
    elif units <= 200:
        bill = (100 * 3) + (units - 100) * 5
    elif units <= 300:
        bill = (100 * 3) + (100 * 5) + (units - 200) * 7
    else:
        bill = (100 * 3) + (100 * 5) + (100 * 7) + (units - 300) * 10

    return bill


def main():
    print("=== Electricity Bill Calculator ===")
    name = input("Customer name: ")
    units = int(input("Units consumed this month: "))

    energy_charge = calculate_bill(units)
    meter_charge = 50
    total = energy_charge + meter_charge

    print("\n----------- BILL -----------")
    print(f"Customer      : {name}")
    print(f"Units used    : {units}")
    print(f"Energy charge : Rs. {energy_charge}")
    print(f"Meter charge  : Rs. {meter_charge}")
    print(f"TOTAL PAYABLE : Rs. {total}")
    print("----------------------------")

    if units > 300:
        print("Tip: Your usage is high. Try switching off unused appliances!")


if __name__ == "__main__":
    main()
