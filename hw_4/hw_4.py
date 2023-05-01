a_int = 13
a_float = 12.0
a_str = "hi"
a_list = []
a_bool = False
a_list.append(a_int)
a_list.append(a_float)
a_list.append(a_str)
a_list.append(a_bool)
print(a_list)
print(a_list[1])
a_tuple = ('qq', 23, 19.0)
a_l_tuple = tuple(a_list)
print(a_l_tuple)
a_dict = {'month1' : 'january', 'month2' : 'february', 'month3' : 'march', 'month4' : 'april', 'month5' : 'may'}
print(a_dict)
other = {'month6' : 'june'}
a_dict.update(other)
print(a_dict.values())
print(a_dict.keys())
print(a_dict)

