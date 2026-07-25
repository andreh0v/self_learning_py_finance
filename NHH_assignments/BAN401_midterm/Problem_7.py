# Problem 7- help plan trip costs

Base_price = 150
Student_price = Base_price * 0.9
group = 0


def discount_factor():
    while True:
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
        choice_B = group * Base_price * (1 - discount_group)
        savings_choice_A = group * Base_price - choice_A
        savings_choice_B = group * Base_price - choice_B
        print(f"choice A costs:{choice_A} ")
        print(f"choice B costs:{choice_B}")
        if choice_A > choice_B:  # The best choice comparer
            print(f"Choice B is the better choice, with a price of {choice_B} & savings of {savings_choice_B}")
        elif choice_B == choice_A:
            print(f"Both cost {choice_A} with savings of {savings_choice_A}")
        else:
            print(f"Choice A is the better choice, with a price of {choice_A} & savings of {savings_choice_A}")
        y_n = input("Do you want to continue? [y/n]")  # Keeps running until it is asked to stop
        if y_n == "y":
            continue
        elif y_n == "n":
            break
        else:
            print("Please enter y or n")
            continue
