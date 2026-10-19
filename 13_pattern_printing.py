"""
Question 13: Pattern Printing
-----------------------------
Nested loops are the heart of this one. Rows = outer loop, columns = inner loop.
"""


def right_triangle(n):
    for i in range(1, n + 1):
        print("* " * i)


def inverted_triangle(n):
    for i in range(n, 0, -1):
        print("* " * i)


def pyramid(n):
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "* " * i
        print(spaces + stars)


def number_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def square(n):
    for _ in range(n):
        print("* " * n)


def main():
    print("=== Pattern Printing ===")
    n = int(input("How many rows? "))

    print("\nRight triangle:")
    right_triangle(n)

    print("\nInverted triangle:")
    inverted_triangle(n)

    print("\nPyramid:")
    pyramid(n)

    print("\nNumber triangle:")
    number_triangle(n)

    print("\nSquare:")
    square(n)


if __name__ == "__main__":
    main()
