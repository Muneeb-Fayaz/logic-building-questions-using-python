"""
Question 1: Armstrong Number
----------------------------
An Armstrong number is a number that equals the sum of its digits,
each raised to the power of the number of digits.

Example: 153 -> 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153  (Armstrong!)
"""


def is_armstrong(number):
    digits = str(number)
    power = len(digits)
    total = 0
    for d in digits:
        total += int(d) ** power
    return total == number


def main():
    print("=== Armstrong Number Checker ===")
    num = int(input("Enter a number: "))

    if is_armstrong(num):
        print(f"Yay! {num} is an Armstrong number.")
    else:
        print(f"Sorry, {num} is not an Armstrong number.")

    # Bonus: show all Armstrong numbers up to 1000
    print("\nAll Armstrong numbers from 1 to 1000:")
    found = [n for n in range(1, 1001) if is_armstrong(n)]
    print(found)


if __name__ == "__main__":
    main()
