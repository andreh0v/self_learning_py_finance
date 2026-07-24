#Sum up transactions amot from input grouped by a cost center cost
def problem4_sol():
    transactions= [{'cc':'A100','amount':200},{'cc':'A100','amount':300},{'cc':'B200','amount':150}]
    summary = {}
    for t in transactions:
        cc = t['cc']
        summary[cc] = summary.get(cc, 0) + t['amount'] #adds everyting, if is not there it will be added + 0 to make sure there are not fails
    print("-" * 25)
    print(f"Summary: {summary}")
    print("-" * 25)
problem4_sol()