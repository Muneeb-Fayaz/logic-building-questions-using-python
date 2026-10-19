"""
Question 8: Fibonacci Series
----------------------------
Each number is the sum of the two before it:
0, 1, 1, 2, 3, 5, 8, 13, 21 ...
"""


def fibonacci(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


def main():
    print("=== Fibonacci Series ===")
    n = int(input("How many terms do you want? "))

    if n <= 0:
        print("Please enter a number greater than 0.")
        return

    result = fibonacci(n)
    print("Here you go:", *result)
    print("Sum of the series:", sum(result))


if __name__ == "__main__":
    main()
