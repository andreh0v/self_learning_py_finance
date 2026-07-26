#Problem 8-simplified mini tax calcuater
Tax=0.22
personal_allowance=100000
def problem_8():
    annual_income = int(input("Enter your annual income: "))
    standard_deduction = min(0.46 * annual_income, 92000)
    taxation= round((annual_income - standard_deduction - personal_allowance)*Tax,2)
    net_annual_income = annual_income - taxation
    if taxation <= 0:
        taxation = 0
    print(f"Your annual income is {annual_income} NOK")
    print("")
    print("=== Mini income tax calculator ===")
    print(f"Your annual income is {annual_income} NOK")
    print(f"Tax (22% of odinary income): {taxation} NOK")
    print("-" * 25)
    print(f"Tax:            {taxation} NOK")
    print(f"Net annual income: {net_annual_income} NOK")
    print(f"Net monthly income: {round(net_annual_income/12,2)}")
problem_8()
