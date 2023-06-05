d = {num: num**2 for num in range(1, 11) if num % 2 == 1}
print(d)

dict_comprehension = {}
for x in range(10):
    if x**3 % 4 == 0:
        dict_comprehension[x] = x**3
print(dict_comprehension)

dict_comprehension = {}
for x in range(10):
    dict_comprehension[x] = x**3 if x**3 % 4 == 0 else x
print(dict_comprehension)

