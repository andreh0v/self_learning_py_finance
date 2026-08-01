#Problem 10 a program that reads the amount of digits.
import re
from collections import Counter
def problem10():
    print("This is a number in sentence counter")
    INPUT = input("Write anything! ")
    digits_only = []

    for char in INPUT:
        if char.isdigit():
            digits_only.append(char)
    number_list = Counter(digits_only)
    print("Digit counter")
    print(f"Input: {INPUT}")
    print("Counts")
    all_counts =[]
    for i in range(0, 10):
        count = number_list.get(str(i), 0)
        all_counts.append(count)
        print(f"{i}: {count}")

    highest_count = max(all_counts)
    most_frequent = []
    for i in range(0, 10):
        count = number_list.get(str(i), 0)
        if count == highest_count:
            most_frequent.append(str(i))

    print(f"Most frequent:", " ".join(most_frequent))

problem10()