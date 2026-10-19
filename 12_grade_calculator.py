"""
Question 12: Student Grade Calculator
-------------------------------------
Take marks of 5 subjects, find total, percentage and grade.

    90 and above -> A+
    80 - 89      -> A
    70 - 79      -> B
    60 - 69      -> C
    50 - 59      -> D
    below 50     -> Fail
"""


def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    return "Fail"


def main():
    print("=== Student Grade Calculator ===")
    name = input("Student name: ")

    total = 0
    for i in range(1, 6):
        marks = float(input(f"Marks in subject {i} (out of 100): "))
        total += marks

    percentage = total / 5
    grade = get_grade(percentage)

    print("\n------ REPORT CARD ------")
    print(f"Name       : {name}")
    print(f"Total      : {total} / 500")
    print(f"Percentage : {percentage:.2f}%")
    print(f"Grade      : {grade}")

    if grade == "Fail":
        print("Don't give up, {}! Practice makes progress.".format(name))
    else:
        print(f"Well done, {name}!")


if __name__ == "__main__":
    main()
