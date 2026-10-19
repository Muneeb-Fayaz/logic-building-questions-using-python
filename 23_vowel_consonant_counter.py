"""
Question 23: Vowel, Consonant, Digit and Space Counter
------------------------------------------------------
Go through a sentence one character at a time and classify each one.
"""


def main():
    print("=== Character Counter ===")
    text = input("Type any sentence: ")

    vowels = consonants = digits = spaces = others = 0

    for ch in text.lower():
        if ch in "aeiou":
            vowels += 1
        elif ch.isalpha():
            consonants += 1
        elif ch.isdigit():
            digits += 1
        elif ch == " ":
            spaces += 1
        else:
            others += 1

    print(f"\nVowels     : {vowels}")
    print(f"Consonants : {consonants}")
    print(f"Digits     : {digits}")
    print(f"Spaces     : {spaces}")
    print(f"Symbols    : {others}")
    print(f"Words      : {len(text.split())}")


if __name__ == "__main__":
    main()
