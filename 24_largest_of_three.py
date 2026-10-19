"""
Question 24: Largest and Smallest of Three Numbers
--------------------------------------------------
Uses plain if/elif logic (no max() or min()) to practise comparisons.
Also checks if the numbers are already in ascending order.
"""


def main():
    print("=== Largest and Smallest ===")
    a = float(input("First number: "))
    b = float(input("Second number: "))
    c = float(input("Third number: "))

    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c

    if a <= b and a <= c:
        smallest = a
    elif b <= a and b <= c:
        smallest = b
    else:
        smallest = c

    print(f"\nLargest  : {largest}")
    print(f"Smallest : {smallest}")

    if a <= b <= c:
        print("They were already in ascending order. Neat!")
    else:
        print("Sorted order:", sorted([a, b, c]))


if __name__ == "__main__":
    main()
