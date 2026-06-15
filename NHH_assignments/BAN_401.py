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


#Problem 2 a model on switching from cobber to fiber
class Region:
    def __init__(self,Region, Length, Incidents_year, Terrain, Permit_Approved):
        self.Region = Region
        self.Length = Length
        self.Incidents_year = Incidents_year
        self.Terrain = Terrain
        self.Permit_Approved = Permit_Approved
Regional_data = {
    "Region Alpha":{
        "Region": "Region_Alpha",
        "Length" : 120,
        "Incidents_year" : 30,
        "Terrain" : "low",
        "Permit_Approved" : True
    },
    "Region Beta":{
        "Region": "Region_Beta",
        "Length" : 200,
        "Incidents_year" : 45,
        "Terrain" : "medium",
        "Permit_Approved" : False
    },
    "Region Gamma":{
        "Region": "Region_Gamma",
        "Length" : 150,
        "Incidents_year" : 60,
        "Terrain" : "high",
        "Permit_Approved" : True
    },
    "Region Delta":{
        "Region": "Region_Delta",
        "Length" : 90,
        "Incidents_year" : 60,
        "Terrain" : "high",
        "Permit_Approved" : True
    },
    "Region Epsilon":{
        "Region": "Region_Epsilon",
        "Length" : 300,
        "Incidents_year" : 90,
        "Terrain" : "high",
        "Permit_Approved" : False
    },
}
copper = {"maintenance_km": 300, "cost_per_incident": 500}
fiber = {"maintenance_km": 100, "cost_per_incident": 100}


if __name__ == "__main__":
    mail_even_func()
    reverse_func()
    print_marked()