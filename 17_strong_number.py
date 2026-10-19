"""
Question 17: Strong Number
--------------------------
A strong number equals the sum of the factorials of its digits.

Example: 145 -> 1! + 4! + 5! = 1 + 24 + 120 = 145  (strong!)
"""


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_strong(n):
    total = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        total += factorial(digit)
        temp //= 10
    return total == n


def main():
    print("=== Strong Number Checker ===")
    n = int(input("Enter a number: "))

    if is_strong(n):
        print(f"{n} is a strong number!")
    else:
        print(f"{n} is not a strong number.")

    print("\nStrong numbers from 1 to 100000:")
    print([x for x in range(1, 100001) if is_strong(x)])


if __name__ == "__main__":
    main()
