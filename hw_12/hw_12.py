foo = lambda x, y: x if x < y else y

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
lst_to_sort.sort()
print(lst_to_sort)

lst_to_sort.sort(reverse=True)
print(lst_to_sort)

#lst_to_sort = list(map(lambda x: x * 2, lst_to_sort))
#print(lst_to_sort)
