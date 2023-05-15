# dict_1 = {'thing':'table', 'name':'Mark', 'day':'wednesday'}
# print(dict_1)
# del dict_1['day']
# dict_1['year'] = '2023'
# print(dict_1)
# list_num = [2014, 8, 1, 2, 30, 3, 5, 21, 27]
# print(list_num)
# list_num.append(2023)
# print(list_num)
# tuple_1 = ('hamster', 2011, False, 23)
# print(tuple_1)
# set_1 = {1, 23, 1, 27,54, 13, 1, 23, 18, 34, 54}
# print(set_1)
# a = 1
# b = 100
# if b>a:
#     print('Умова виконується')
# if b<a:
#     print('Умова не виконується')
# if b != a:
#     print('Умова не виконується')
#
# num_1 = float(input("Введіть число: "))
# if num_1 > 0:
#         print("Число є додатнім")
# elif num_1 < 0:
#         print("Число є від'ємним")
# else:
#     print('Введене число дорівнює 0')
#
# 12.Визначити в якій четверті координотних вісей знаходиться точка з заданими координатами х та у().x > 0, y > 0 — перша
# четверть
#
x = float(input("Введіть координату x:"))
y = float(input("Введіть координату y:"))

if x > 0 and y > 0:
    print("Точка знаходиться в першій четверті координатних вісей")
elif x < 0 and y > 0:
    print("Точка знаходиться в другій четверті координатних вісей")
elif x < 0 and y < 0:
    print("Точка знаходиться в третій четверті координатних вісей")
elif x > 0 and y < 0:
    print("Точка знаходиться в четвертій чверті координатних вісей")
elif x == 0 and y == 0:
    print("Координата точки = (0;0)")
elif x > 0 or x < 0 and y == 0:
    print("Точка знаходиться на вісі x")
elif x == 0 and y < 0 or y >0:
    print("Точка знаходиться на вісі y")
else:
    print("Точка знаходиться на вісі x або y")
# num_a = float(input("Введіть перше число: "))
# num_b = float(input("Введіть друге число: "))
# if num_a>num_b:
#     print(num_b)
# else:
#     print(num_a)