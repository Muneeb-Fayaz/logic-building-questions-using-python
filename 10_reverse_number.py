"""
Question 10: Reverse a Number
-----------------------------
Example: 1234 -> 4321

Idea: keep picking the last digit with % 10 and build the new number.
"""


def reverse_number(n):
    reversed_num = 0
    while n > 0:
        last_digit = n % 10
        reversed_num = reversed_num * 10 + last_digit
        n = n // 10
    return reversed_num


def main():
    print("=== Reverse a Number ===")
    n = int(input("Enter a positive number: "))

    if n < 0:
        print("Let's keep it positive, please!")
        return

    print(f"Reverse of {n} is {reverse_number(n)}")


if __name__ == "__main__":
    main()
