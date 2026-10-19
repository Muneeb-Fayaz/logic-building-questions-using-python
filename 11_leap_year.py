"""
Question 11: Leap Year
----------------------
A year is a leap year if:
  - it is divisible by 4, AND
  - NOT divisible by 100, unless it is also divisible by 400.

Examples: 2024 yes, 1900 no, 2000 yes.
"""


def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def main():
    print("=== Leap Year Checker ===")
    year = int(input("Enter a year: "))

    if is_leap(year):
        print(f"{year} is a leap year. February has 29 days!")
    else:
        print(f"{year} is not a leap year. February has 28 days.")


if __name__ == "__main__":
    main()
