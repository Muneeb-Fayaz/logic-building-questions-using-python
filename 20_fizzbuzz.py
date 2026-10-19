"""
Question 20: FizzBuzz
---------------------
For numbers 1 to N:
  - multiple of 3          -> print "Fizz"
  - multiple of 5          -> print "Buzz"
  - multiple of both       -> print "FizzBuzz"
  - otherwise              -> print the number

A classic interview question!
"""


def main():
    print("=== FizzBuzz ===")
    n = int(input("Count up to: "))

    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == "__main__":
    main()
