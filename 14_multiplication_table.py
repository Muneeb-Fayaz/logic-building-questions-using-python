"""
Question 14: Multiplication Table
---------------------------------
Print the table of any number up to any length.
"""


def main():
    print("=== Multiplication Table ===")
    n = int(input("Which number's table do you want? "))
    upto = int(input("Up to how many terms? (e.g. 10) "))

    print(f"\nTable of {n}:")
    for i in range(1, upto + 1):
        print(f"{n} x {i:2} = {n * i}")


if __name__ == "__main__":
    main()
