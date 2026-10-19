# 🐍 Python Logic Building Practice

### Think logically. Write simple code. Become a better programmer.

A beginner-friendly collection of **24 Python programs** designed to improve logical thinking, problem-solving skills, and programming fundamentals.

This repository is built for students and beginners who want to understand how Python works by practising real coding problems — one program at a time.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python 3">
  <img src="https://img.shields.io/badge/Programs-24-orange?style=for-the-badge" alt="24 Programs">
  <img src="https://img.shields.io/badge/Level-Beginner-success?style=for-the-badge" alt="Beginner Level">
  <img src="https://img.shields.io/badge/Status-Learning%20%26%20Practice-purple?style=for-the-badge" alt="Learning and Practice">
</p>

---

## ✨ About This Project

Learning Python is not just about memorising syntax. It is about learning how to break a problem into small steps and turn those steps into working code.

That is exactly what this repository is for.

Every program includes a short explanation, friendly input prompts, and readable code with simple comments wherever useful.

**The goal is simple:** understand the logic, practise regularly, and gradually become confident at solving problems on your own.

## 🚀 Getting Started

You only need Python installed on your computer.

**1. Clone this repository**

```bash
git clone YOUR_REPOSITORY_URL
```

**2. Open the project folder**

```bash
cd python-logic-building-practice
```

**3. Run any Python program**

```bash
python 01_armstrong_number.py
```

You can also open the files in VS Code and run them individually.

> Replace `YOUR_REPOSITORY_URL` with your actual GitHub repository URL.

---

## 📚 Programs Included

| # | Python File | What You'll Practise |
|:--:|---|---|
| 01 | `01_armstrong_number.py` | Armstrong number logic |
| 02 | `02_atm_machine.py` | PIN, deposits and withdrawals |
| 03 | `03_electricity_bill.py` | Electricity bill using unit slabs |
| 04 | `04_palindrome.py` | Palindrome numbers and strings |
| 05 | `05_prime_numbers.py` | Prime checks and prime ranges |
| 06 | `06_odd_series.py` | Odd number series |
| 07 | `07_even_series.py` | Even number series |
| 08 | `08_fibonacci_series.py` | Fibonacci sequence |
| 09 | `09_factorial.py` | Factorial using loops and recursion |
| 10 | `10_reverse_number.py` | Reversing a number |
| 11 | `11_leap_year.py` | Leap year conditions |
| 12 | `12_grade_calculator.py` | Marks, percentages and grades |
| 13 | `13_pattern_printing.py` | Star and number patterns |
| 14 | `14_multiplication_table.py` | Multiplication tables |
| 15 | `15_gcd_lcm.py` | GCD and LCM calculations |
| 16 | `16_perfect_number.py` | Perfect number checking |
| 17 | `17_strong_number.py` | Strong number checking |
| 18 | `18_sum_of_digits.py` | Digit sum, digit count and digital root |
| 19 | `19_number_guessing_game.py` | Number guessing game |
| 20 | `20_fizzbuzz.py` | Conditions and loops with FizzBuzz |
| 21 | `21_simple_calculator.py` | Basic arithmetic operations |
| 22 | `22_temperature_converter.py` | Celsius and Fahrenheit conversion |
| 23 | `23_vowel_consonant_counter.py` | Vowels, consonants and character counting |
| 24 | `24_largest_of_three.py` | Largest and smallest of three numbers |

---

## 🧠 Concepts You'll Learn

By working through these programs, you can practise:

- **Variables and data types** — storing and using information.
- **Input and output** — interacting with users through the terminal.
- **If-else conditions** — making decisions in your code.
- **Loops** — repeating instructions efficiently.
- **Strings and numbers** — solving common programming problems.
- **Functions and recursion** — organising reusable logic.
- **Basic arithmetic** — applying formulas to everyday problems.
- **Problem-solving** — breaking bigger questions into smaller steps.

## 💻 Example: Armstrong Number

An Armstrong number is a number equal to the sum of its digits raised to the power of the number of digits.

For example:

`153 = 1³ + 5³ + 3³ = 153`

Here is a simple Python implementation:

```python
# Check whether a number is an Armstrong number

number = int(input("Enter a number: "))

digits = str(number)
power = len(digits)
total = 0

for digit in digits:
    total = total + int(digit) ** power

if number >= 0 and total == number:
    print("It is an Armstrong number.")
else:
    print("It is not an Armstrong number.")
```

This example demonstrates how loops, strings, conditions, and basic mathematics can work together to solve a problem.

## 🎯 How to Practise Effectively

1. Read the question carefully.
2. Try to solve it yourself before opening the solution.
3. Write down the steps in plain English.
4. Run the program with different inputs.
5. Test edge cases such as `0`, negative numbers, and repeated values where relevant.
6. Rewrite the solution without looking at the original code.

Don't worry if you cannot solve a question on your first attempt. The purpose of practice is to improve your thinking, not to get everything right immediately.

## 🛠️ Tools Used

- **Language:** Python 3
- **Editor:** Visual Studio Code (recommended)
- **Version Control:** Git and GitHub

No external Python libraries are required for the core exercises unless a specific program states otherwise.

## 🌱 Who Is This For?

- Students learning Python for the first time.
- Beginners practising programming fundamentals.
- College students preparing for practical exams.
- Anyone who wants to improve logical thinking through coding.

## 🤝 Contributions

Have a simpler solution, a useful explanation, or another beginner-friendly problem?

Feel free to fork the repository, improve the code, and submit a pull request. Keep contributions readable and easy for beginners to understand.

## ⭐ Support

If this repository helps you learn Python, consider giving it a **star ⭐** on GitHub. It helps others discover the project, too.

---

<p align="center">
  <b>Keep practising. Keep experimenting. Keep building. 🚀</b>
  <br>
  <i>One problem at a time, one step closer to becoming a better programmer.</i>
</p>
