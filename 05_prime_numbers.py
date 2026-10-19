"""
Question 5: Prime Numbers
-------------------------
A prime number is greater than 1 and divisible only by 1 and itself.
Examples: 2, 3, 5, 7, 11, 13 ...

Part A: Check if one number is prime.
Part B: Print all primes in a range.
"""


def is_prime(n):
    if n < 2:
        return False
    # We only need to check up to the square root of n
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def main():
    print("=== Prime Number Fun ===")

    n = int(input("Is this number prime? Enter it: "))
    if is_prime(n):
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")

    start = int(input("\nPrint primes from: "))
    end = int(input("Up to: "))

    primes = [x for x in range(start, end + 1) if is_prime(x)]
    print(f"Primes between {start} and {end}: {primes}")
    print(f"That's {len(primes)} prime numbers in total.")


if __name__ == "__main__":
    main()
