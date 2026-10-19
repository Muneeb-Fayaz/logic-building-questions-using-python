"""
Question 2: ATM Machine
-----------------------
Build a tiny ATM with PIN check, balance, deposit and withdraw.

Rules:
- You get 3 attempts to enter the correct PIN.
- You can't withdraw more than your balance.
- Amounts must be positive.
"""

CORRECT_PIN = 1234


def check_pin():
    for attempt in range(1, 4):
        pin = int(input(f"Enter your 4-digit PIN (attempt {attempt}/3): "))
        if pin == CORRECT_PIN:
            print("PIN accepted. Welcome!\n")
            return True
        print("Oops, wrong PIN.")
    print("Too many wrong attempts. Your card is blocked. Please visit the bank.")
    return False


def main():
    print("=== Welcome to Python Bank ATM ===")
    if not check_pin():
        return

    balance = 10000

    while True:
        print("\nWhat would you like to do?")
        print("1. Check balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Exit")
        choice = input("Choose 1-4: ")

        if choice == "1":
            print(f"Your balance is Rs. {balance}")

        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                print("Please enter a positive amount.")
            else:
                balance += amount
                print(f"Deposited Rs. {amount}. New balance: Rs. {balance}")

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Please enter a positive amount.")
            elif amount > balance:
                print("Not enough balance, sorry!")
            else:
                balance -= amount
                print(f"Please collect Rs. {amount}. Remaining balance: Rs. {balance}")

        elif choice == "4":
            print("Thank you for banking with us. Have a great day!")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
