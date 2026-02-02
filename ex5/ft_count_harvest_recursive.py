def ft_count_from_one_to_num(num):
    if num == 1:
        print(f"Day {num}")
        return 1
    ft_count_from_one_to_num(num - 1)
    print(f"Day {num}")


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    ft_count_from_one_to_num(days)
    print("Harvest time!")
