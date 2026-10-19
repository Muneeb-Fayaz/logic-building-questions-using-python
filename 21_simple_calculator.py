"""
Question 21: Simple Calculator
------------------------------
Supports + - * / % and ** with friendly error handling.
Keeps running until you type 'q'.
"""


def calculate(a, op, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Oops! You can't divide by zero."
        return a / b
    elif op == "%":
        if b == 0:
            return "Oops! You can't take a remainder with zero."
        return a % b
    elif op == "**":
        return a ** b
    return "Unknown operator. Use + - * / % or **"


def main():
    print("=== Simple Calculator ===  (type q to quit)")
    while True:
        first = input("\nFirst number: ")
        if first.lower() == "q":
            break
        op = input("Operator (+ - * / % **): ")
        second = input("Second number: ")

        try:
            result = calculate(float(first), op, float(second))
            print("Answer:", result)
        except ValueError:
            print("Please type valid numbers.")

    print("Bye! Happy calculating.")


if __name__ == "__main__":
    main()
