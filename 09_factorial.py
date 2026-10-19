"""
Question 9: Factorial
---------------------
n! = n x (n-1) x (n-2) x ... x 1
Example: 5! = 5 x 4 x 3 x 2 x 1 = 120
(and 0! is defined as 1)
"""


def factorial_loop(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


def main():
    print("=== Factorial Calculator ===")
    n = int(input("Enter a number: "))

    if n < 0:
        print("Factorial isn't defined for negative numbers.")
        return

    steps = " x ".join(str(i) for i in range(n, 0, -1)) or "1"
    print(f"{n}! = {steps} = {factorial_loop(n)}")
    print(f"(Recursion gives the same answer: {factorial_recursive(n)})")


if __name__ == "__main__":
    main()
