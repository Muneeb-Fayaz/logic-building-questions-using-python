"""
Question 16: Perfect Number
---------------------------
A perfect number equals the sum of its proper divisors (divisors except itself).

Example: 6 -> 1 + 2 + 3 = 6   (perfect!)
         28 -> 1 + 2 + 4 + 7 + 14 = 28
"""


def proper_divisors(n):
    return [i for i in range(1, n) if n % i == 0]


def main():
    print("=== Perfect Number Checker ===")
    n = int(input("Enter a number: "))

    divisors = proper_divisors(n)
    total = sum(divisors)
    print(f"Divisors of {n} (excluding itself): {divisors}")
    print(f"Their sum: {total}")

    if total == n and n > 1:
        print(f"{n} is a perfect number!")
    else:
        print(f"{n} is not a perfect number.")

    print("\nPerfect numbers up to 10000:")
    print([x for x in range(2, 10001) if sum(proper_divisors(x)) == x])


if __name__ == "__main__":
    main()
