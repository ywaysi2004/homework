#1!
def multiply_numbers(a, b = 2):
    return a * b
print(multiply_numbers(5, 2))

#2

def print_arguments(*args):
    for arg in args:
        print(arg)
result_second = print_arguments(1, 2, 3, 4, 5)

#3

def str_args(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
print(str_args(name = "Joseph", age = 54, city = "Barcelona"))

###None
###4
###None

import math

def cal_triangle(a, b, c):
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area
print(cal_triangle(7, 8, 9))