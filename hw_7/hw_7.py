numbers = [12, 25, 98, 156, 36, 87]
i = 0

for num in numbers:
    i += num

print("Сума чисел в списку:", i)

names = ["Ann", "Oxy", "Vova", "Eva", "Michael"]

for index, name in enumerate(names):
    print("Індекс:", index, "Ім'я:", name)


x = int(input("Введіть число х:"))
squares = []

for num in range(1, x):
    if num > 0:
        squares.append(num ** 2)

print("Квадрати додатних чисел менших за", x, ":", squares)


for num in range(15, 0, -1):
    print(num)


numbers = dict(zip([1, 2, 3], ['One', 'Two', 'Three']))
print(numbers)


a = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four'}
b = {5, 6, 7, 8}
result = {a, dict.fromkeys(b)}

print(result)