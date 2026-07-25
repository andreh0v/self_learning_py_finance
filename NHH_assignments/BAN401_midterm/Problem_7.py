# Problem 7- help plan trip costs

Base_price = 150
Student_price = Base_price * 0.9
group = 0


def problem_7():
    while True:
        print("*"*25)
        print("* Welcome to the Discount Calculator! *")
        print(*"Calculate your expenses easily! *")
        print("*"*25)
        students = int(input("Enter total students: "))
        non_students = int(input("Enter total non-students: "))
        group = students + non_students
        choice_A = Student_price * students + non_students * Base_price
        if group >= 50:  # Finds the right discount for group size
            discount_group = 0.07
        elif group >= 30:
            discount_group = 0.03
        elif group >= 20:
            discount_group = 0.02
        elif group >= 10:
            discount_group = 0.01
        else:
            discount_group = 0.0
        choice_B = round(group * Base_price * (1 - discount_group),2)
        savings_choice_A = round(group * Base_price - choice_A,2)
        savings_choice_B = round(group * Base_price - choice_B,2)
        print("---Summary---")
        print(f"Base price per person {Base_price}")
        print(f"People total {group} (students={students}, non-students={non_students})")
        print(f"Base total (no discounts) : {Base_price * group}")
        print("")
        print(f"Scenario A -Student % discount only")
        print(f"Total: ${choice_A} | savings vs base: ${choice_A}")
        print("")
        print(f"Scenario B - Volume % discount only (tier for {group} -> {discount_group})")
        print(f"Total: ${choice_B} | savings vs base: ${choice_B}")
        print(f"Choice B costs:{choice_B}")
        print("=== Best option ===")
        if choice_A > choice_B:  # The best choice comparer
            print(f"Volume discount: ${choice_B} (better by: {savings_choice_B})")
        elif choice_B == choice_A:
            print(f"Both cost {choice_A} savings {savings_choice_A}")
        else:
            print(f"Choice A is the better choice, with a price of {choice_A} & savings of {savings_choice_A}")
        print("*" * 25)
        y_n = input("Do you want to continue? [y/n]")  # Keeps running until it is asked to stop
        if y_n == "y":
            continue
        elif y_n == "n":
            print("Bye!")
            break
        else:
            print("Please enter y or n")
            continue
problem_7()