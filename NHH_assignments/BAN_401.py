#BAN401 endterm assignment Applied Programming and Data Analysis for Business
#Problem 1
#Step 1 Sending mail to even numbers

customers = list(range(1,1001))
customer_status = [0] * 1000

def mail_even_func():
    for number in range(1, 1001):
        if number % 2 == 0:
            customer_status [number - 1] =1
#Step 2 Reverse
def reverse_func():
    for i in range (1,21):
        for j in customers:
         if j % i == 0:
            if customer_status[j - 1] == 1:
                customer_status[j - 1] = 0
            elif customer_status[j - 1] == 0:
                customer_status[j - 1] = 1
def print_marked():
    count = 0
    for index in range(1000):
        if customer_status[index] == 1:
            count += 1
            print(index + 1, end =" ")
            if count == 30:
                break


#Problem 2 a model on switching from cobber to fiberclass Region_total:
class Region:
        def __init__(self, name, length, incidents_year, terrain, permit_approved):
            self.name = name
            self.length = length
            self.incidents_year = incidents_year
            self.terrain = terrain
            self.permit_approved = permit_approved
regions = [
    Region("Alpha", 120, 30, "low", True),
    Region("Beta", 200, 45, "medium", False),
    Region("Gamma", 150, 60, "high", True),
    Region("Delta", 90, 20, "medium", True),
    Region("Epsilon", 300, 90, "high", False)
]
copper = {"maintenance_km": 300, "cost_per_incident": 500}
fiber = {"maintenance_km": 100, "cost_per_incident": 100}

terrain_multiplier = {"low": 1.0, "medium": 1.2, "high": 1.5}

#3 Operating cost
def operating_cost(length, incidents, terrain, network):
    multiplier = terrain_multiplier[terrain]
    cost = (length * network["maintenance_km"] * multiplier) + (incidents * network["cost_per_incident"])
    return cost

#Fiber development constrains
def feasible(terrain, permit_approved):
    if terrain == "high" and permit_approved == False:
        return False
    else:
        return True
def process_region(region):
        copper_cost = operating_cost(region.length, region.incidents_year, region.terrain, copper)
        fiber_cost = operating_cost(region.length, region.incidents_year, region.terrain, fiber)
        feasible_result = feasible(region.terrain, region.permit_approved)
        if feasible_result ==False:
            fiber_cost = "N/A"
            savings = "N/A"
            recommendation ="Fiber not Feasible"
        else:
            savings = copper_cost-fiber_cost
            if savings >= 0:
                recommendation = "Switch to fiber"
            else:
                recommendation = "Stay on copper"
        print(f"""Region:\t{region.name}
          Terrain:\t{region.terrain}
          Permit Approved:\t{region.permit_approved}
          Fiber Feasible?:\t{feasible_result}
          Copper Cost:\tNOK {copper_cost}
          Fiber Cost:\tNOK {fiber_cost}
          Savings:\tNOK {savings}
          Recommendation:\t{recommendation}
        """)
#Problem 3
if __name__ == "__main__":
    mail_even_func()
    reverse_func()
    print_marked()
    for region in regions:
        process_region(region)