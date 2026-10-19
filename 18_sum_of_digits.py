"""
Question 18: Sum and Count of Digits
------------------------------------
Example: 1234 -> digits = 4, sum = 1+2+3+4 = 10
Also finds the digital root (keep adding until one digit is left).
"""


def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def digital_root(n):
    while n >= 10:
        n = sum_of_digits(n)
    return n


def main():
    print("=== Digit Magic ===")
    n = int(input("Enter a positive number: "))

    print(f"Number of digits : {len(str(n))}")
    print(f"Sum of digits    : {sum_of_digits(n)}")
    print(f"Digital root     : {digital_root(n)}")


if __name__ == "__main__":
    main()
