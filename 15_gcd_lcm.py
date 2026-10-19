"""
Question 15: GCD (HCF) and LCM
------------------------------
GCD = biggest number that divides both numbers.
LCM = smallest number that both numbers divide into.

Relation: GCD x LCM = a x b
We use Euclid's algorithm for GCD: keep replacing (a, b) with (b, a % b).
"""


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


def main():
    print("=== GCD and LCM ===")
    a = int(input("First number: "))
    b = int(input("Second number: "))

    print(f"GCD (HCF) of {a} and {b} = {gcd(a, b)}")
    print(f"LCM of {a} and {b} = {lcm(a, b)}")


if __name__ == "__main__":
    main()
