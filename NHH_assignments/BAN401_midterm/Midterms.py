
#Problem 1
def problem1_trip():
    total_trips_toll = 0
    total_days = int(input("How many days did you drive across Sotrabrua this week? "))
    for i in range(0, total_days):
        day_trips = int(input(f"Day {i+1}: How many times did you pass the toll? "))
        total_trips_toll += day_trips
    print("-" * 25)
    print(f"You passed {total_trips_toll} times in {total_days} days.")
    print(f"That is for a cost of {total_trips_toll * 35} kr at 35 kr a trip.")
if __name__ == "__main__":
    problem1_trip()
