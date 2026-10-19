"""
Question 4: Palindrome (Number and String)
------------------------------------------
A palindrome reads the same forwards and backwards.
Examples: 121, 1331, "madam", "level"
"""


def is_palindrome_number(n):
    original = n
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return original == reversed_num


def is_palindrome_string(text):
    # Ignore spaces and capital letters so "Nitin" and "A man a plan" style works
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def main():
    print("=== Palindrome Checker ===")

    num = int(input("Enter a number: "))
    if is_palindrome_number(num):
        print(f"{num} is a palindrome number!")
    else:
        print(f"{num} is NOT a palindrome number.")

    word = input("\nNow enter a word or sentence: ")
    if is_palindrome_string(word):
        print(f'"{word}" is a palindrome!')
    else:
        print(f'"{word}" is NOT a palindrome.')


if __name__ == "__main__":
    main()
