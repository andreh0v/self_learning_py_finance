#Problem 9 - A program that help restaurants review hos sales develop during the week
day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
def sales_stats(sales_list):
    lowest = min(sales_list)
    highest = max(sales_list)
    average = sum(sales_list) / len(sales_list)
    return lowest, highest, average
def problem_9():
    sales_a_day = []
    for day in day_names:
        today_sales = round(float(input(f"Enter sales {day}: ")),2)
        sales_a_day.append(today_sales)
    min_sales, max_sales, avg_sales = sales_stats(sales_a_day)
    min_index = sales_a_day.index(min_sales)
    min_day = day_names[min_index]
    max_index = sales_a_day.index(max_sales)
    max_day = day_names[max_index]
    print("-"*25)
    for name, sales in zip(day_names, sales_a_day):#An AI based solution learning me about zip.
        print(f"{name}: {sales} NOK")

    print(f"Total sales: {sum(sales_a_day)} NOK")
    print(f"Average daily sales: {avg_sales:.2f} NOK")
    print(f"Lowest sales: {min_sales} NOK (day: {min_day})")
    print(f"Highest sales: {max_sales} NOK (day: {max_day})")

problem_9()