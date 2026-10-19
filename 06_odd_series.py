"""
Question 6: Odd Number Series
-----------------------------
Print the first N odd numbers, their sum, and all odd numbers in a range.

Fun fact: the sum of the first N odd numbers is always N * N.
"""


def main():
    print("=== Odd Series ===")

    n = int(input("How many odd numbers do you want? "))

    odds = []
    current = 1
    for _ in range(n):
        odds.append(current)
        current += 2

    print("Odd series:", *odds)
    print("Sum of these numbers:", sum(odds))
    print(f"Check: {n} x {n} = {n * n}  (matches the fun fact!)")

    start = int(input("\nPrint odd numbers from: "))
    end = int(input("Up to: "))
    print(f"Odd numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if num % 2 != 0:
            print(num, end=" ")
    print()


if __name__ == "__main__":
    main()
