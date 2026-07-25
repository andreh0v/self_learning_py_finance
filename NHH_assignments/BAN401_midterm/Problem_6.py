#Problem 6-calculates how much you have spent & convert everything to NOK
def ex_rate_thing(ex_r):
    ex_rate = {"EUR":11.5, "USD":10.6, "SEK": 1.0}
    return ex_rate[ex_r]


def problem_6_sol():
    valid_EX = ["EUR", "USD", "SEK"]
    posted_EX = {}
    print("Enter your 'amount' & 'currency'! Type 'done' to get your final calc")

    while True:
        answer = input("'amount' & 'currency', or are you done? ")

        if answer.lower() == "done":
            break
        else:
            parts = answer.split()
            if len(parts) != 2:#Fail-switch for both currency & amount
                print("try again with a currency or an amount")
                continue
            else:
                amount_string, currency = answer.split()#splitting into the currency & amount, in line with the dict
                if currency.upper() in valid_EX:
                    posted_EX[currency.upper()] = posted_EX.get(currency.upper(), 0) + float(amount_string)#adding it to the final dict, with text returend as numbs
                else:
                    print("Please enter either 'EUR', 'USD' or 'SEK'")
                    continue

    if len(posted_EX) == 0:
        print("You have not entered amount & ex")
    else:
        total_nok = 0
        for cur, subtotal in posted_EX.items(): #going through each currency with its subtotal, returning it
            print(cur, ":", subtotal)
            total_nok += ex_rate_thing(cur) * subtotal #converting it to nok
        print(f"{total_nok} NOK")


problem_6_sol()


