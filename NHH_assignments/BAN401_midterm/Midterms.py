from os import WCONTINUED

from matplotlib import container


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

#Problem 2
def problem2_trip():
    total_hours = 0
    no_command = ["NO","no", "N", "n", "Nei", "NEI" ]
    intensity_cals = {"easy" : 300, "medium": 450, "hard": 600}
    total_hours = int(input("How many hours did you walk up Ulriken? "))
    if total_hours > 0:
        Yes_no = input("Where they all the same insensity?")
        if Yes_no in no_command:
            while True:
                easy_hours = int(input("How many of the hours where a easy intensity?"))
                normal_hours = int(input("How many of the hours where normal intensity?"))
                hard_hours = int(input("How many of the hours where a hard intensity?"))
                if easy_hours + normal_hours + hard_hours < 0:
                    print("cant walk negative hours!")
                    continue
                elif easy_hours + normal_hours + hard_hours == 0:
                   print("You did not walk Ulriken!")
                   continue
                elif easy_hours + normal_hours + hard_hours != total_hours:
                    print(f"You said you walked {total_hours} hours!")
                    continue
                else:
                    total_cals_burned=easy_hours * intensity_cals["easy"] + normal_hours * intensity_cals["medium"] + hard_hours * intensity_cals["hard"]
                    print(f"Calories burned {total_cals_burned} calories.")
                    break
        else:
            intensity = input("What was the intensity (easy/medium/hard): ?")
            print(f"calories burned {intensity_cals[intensity] * total_hours}kcal")


    else:
        print("You did not walk Ulriken! You should try it!")

problem2_trip()

#if __name__ == "__main__":
    #problem1_trip()