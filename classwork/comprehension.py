list_1 = []
list_2 = []

for num in range(10):
    if num % 2 == 1:
        list_1.append(num ** 2)
    else:
        list_1.append(num ** 4)

list_compreh = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print('Comprehension:', list_compreh)

print((list_1))


list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
print(list_comprehension)

list_compr1 = []
for num in range(10):
    if num % 2 == 0:
        list_compr1.append(num // 2)
    else:
        list_compr1.append(num * 10)
print(list_compr1)

print("***" * 10)

d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
    else:
        d[num] = num // 0.5
print(d)

dict_compreh1 = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(dict_compreh1)