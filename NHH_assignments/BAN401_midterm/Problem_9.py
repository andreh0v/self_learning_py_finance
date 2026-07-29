#Problem 9 - A program that help restaurants review hos sales develop during the week
day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def problem_9():
    sales_a_day = []
    for day in day_names:
        today_sales = round(float(input(f"Enter sales {day}: ")),2)
        sales_a_day.append(today_sales)
    for day in day_names:
        print(f"Sales day {day}: NOK {today_sales}")
    print("WEEKLY SALES")
    print(f"Total sales: {sum(sales_a_day)} NOK")
    print(f"Average daily sales: {sum(sales_a_day)/len(sales_a_day):.2f)} NOK")

problem_9()