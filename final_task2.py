def recursive_sum(lst):
    if not lst:
        return 0
    else:
        return lst[0] + recursive_sum(lst[1:])

my_list = [1, 2, 3, 4, 5]
result = recursive_sum(my_list)
print("The sum of the elements in the list is:", result)
