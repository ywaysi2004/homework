#1
numbers = []
for x in range(10):
    numbers.append(x)
print(numbers)
#2
squares = []
for x in range(1, 6):
    squares.append(x ** 2)
print(squares)
#3
even_numbers = []
for x in range(15):
    if x % 2 == 1:
        even_numbers.append(x)
print(even_numbers)
#4
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [f"{number} is even" if number % 2 == 0 else f"{number} is odd" for number in numbers]
print(result)
#5
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = {x: x**2 for x in numbers if x % 2 == 0}
print(even_squares)
#6
def email_name(email):
    username = email.split('@')[0]
    name = username.split('.')[0]
    return name
email = 'max@gmail.com'
name = email_name(email)
print(name)
#7
def c_el(*args):
    return len(args)
result = c_el(1, 2,'a')
print(result)
#8
def add_to_list(**kwargs):
    values = []
    for arg_name, arg_value in kwargs.items():
        values.append(arg_value)
    return values
result = add_to_list(arg1='obama', arg2=123, arg3='John')
print(result)