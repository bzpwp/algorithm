from itertools import islice

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
group_count = 3

iter_list = iter(my_list)
grouped_list = [list(islice(iter_list, len(my_list) // group_count)) for _ in range(group_count)]

print("Grouped List:", grouped_list)
