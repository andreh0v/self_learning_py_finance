#Problem 5 - A program calculating GPA
def grade_to_points(letter_grade):
    points = {"A": 5, "B": 4, "C": 3, "D": 2, "E": 1, "F": 0}
    return points[letter_grade]

def gpa_func():
    valid_grades = ["A", "B", "C", "D", "E", "F"]
    grades = []

    print("Eneter your grades (A-F). Typde 'done' when finished.")

    while True:
        answer = input("Enter grade: ").strip()
        if answer.lower() == "done":
            break
        elif answer.upper() in valid_grades:
            grades.append(answer.upper())
        else:
            print("Invalid input. Please enter A-F or 'done'.")
    if len(grades) == 0:
        print("No grades were entered.")
    else:
        order = "ABCDEF"
        sorted_grades = sorted(grades, key=lambda x:order.index(x))
        print(f"Your grades: {sorted_grades}")

        total_points = sum(grade_to_points(x) for x in sorted_grades)
        gpa = total_points / len(sorted_grades)
        print(f"Your GPA: {round(gpa,2)}")
gpa_func()