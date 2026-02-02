def ft_plant_age():
    age_of_harvest = int(input("Enter plant age in days: "))
    if age_of_harvest > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
