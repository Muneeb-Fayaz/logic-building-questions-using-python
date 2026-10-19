"""
Question 19: Number Guessing Game
---------------------------------
The computer thinks of a number between 1 and 100.
You get 7 tries, and it tells you "higher" or "lower" after each guess.
"""

import random


def main():
    print("=== Number Guessing Game ===")
    secret = random.randint(1, 100)
    max_tries = 7

    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_tries} tries. Good luck!\n")

    for attempt in range(1, max_tries + 1):
        guess = int(input(f"Try {attempt}: "))

        if guess == secret:
            print(f"Wow, you got it in {attempt} tries! The number was {secret}.")
            break
        elif guess < secret:
            print("Too low, go higher.")
        else:
            print("Too high, go lower.")
    else:
        print(f"\nOut of tries! The number was {secret}. Better luck next time.")


if __name__ == "__main__":
    main()
