"""
Question 22: Temperature Converter
----------------------------------
Celsius <-> Fahrenheit <-> Kelvin

    F = C x 9/5 + 32
    K = C + 273.15
"""


def main():
    print("=== Temperature Converter ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    choice = input("Choose 1-3: ")

    temp = float(input("Enter the temperature: "))

    if choice == "1":
        print(f"{temp} C = {temp * 9 / 5 + 32:.2f} F")
    elif choice == "2":
        print(f"{temp} F = {(temp - 32) * 5 / 9:.2f} C")
    elif choice == "3":
        print(f"{temp} C = {temp + 273.15:.2f} K")
    else:
        print("Invalid choice.")
        return

    # A little humanised weather comment (based on Celsius input)
    if choice in ("1", "3"):
        if temp < 10:
            print("Brrr, that's cold. Grab a jacket!")
        elif temp < 30:
            print("Nice and pleasant weather.")
        else:
            print("Phew, it's hot! Stay hydrated.")


if __name__ == "__main__":
    main()
