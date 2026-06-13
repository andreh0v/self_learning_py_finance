#BAN401 endterm assignment Applied Programming and Data Analysis for Business

#Problem 1 Sending mail to odd numbers
def mail_even_func():
    for number in range(0, 1000):
        if number % 2 == 0:
            print("Send mail")

mail_even_func()