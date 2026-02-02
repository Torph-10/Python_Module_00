def ft_count_harvest_iterative():
    remain_days = int(input("Days until harvest: "))
    for day in range(1, remain_days+1):
        print(f"Day {day}")
    print("Harvest time!")
