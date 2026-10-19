"""
Question 7: Even Number Series
------------------------------
Print the first N even numbers, their sum, and all even numbers in a range.

Fun fact: the sum of the first N even numbers is always N * (N + 1).
"""


def main():
    print("=== Even Series ===")

    n = int(input("How many even numbers do you want? "))

    evens = []
    current = 2
    for _ in range(n):
        evens.append(current)
        current += 2

    print("Even series:", *evens)
    print("Sum of these numbers:", sum(evens))
    print(f"Check: {n} x {n + 1} = {n * (n + 1)}  (matches the fun fact!)")

    start = int(input("\nPrint even numbers from: "))
    end = int(input("Up to: "))
    print(f"Even numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(num, end=" ")
    print()


if __name__ == "__main__":
    main()
