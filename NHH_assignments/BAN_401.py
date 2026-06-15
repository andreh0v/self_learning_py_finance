#BAN401 endterm assignment Applied Programming and Data Analysis for Business
#Problem 1
#Step 1 Sending mail to even numbers
customer_status = [0] * 1000
customers = list(range(1,1001))
def mail_even_func():
    for number in range(1, 1001):
        if number % 2 == 0:
            customer_status [number - 1] =1
#Step 2 Reverse
def reverse_func():
    for i in range (1,21):
        for j in customers:
         if j % i == 0:
            if customer_status[j-1] == 1:
                customer_status[j-1] = 0
            elif customer_status[j-1] == 0:
                customer_status[j-1] = 1
def print_marked():
    count = 0
    for index in range(1000):
        if customer_status[index] == 1:
            count += 1
            print(index + 1)
            if count == 30:
                break
mail_even_func()
reverse_func()
print_marked()