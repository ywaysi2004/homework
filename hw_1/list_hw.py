e_list = ['attemp', 'developer', 'banana', 'cinnamon', 'breezy']
print(sorted(e_list))

del e_list[4]
print(e_list)

print(e_list.index('banana'))

b_list = ['vero', 'twice']
e_list.extend(b_list)
print(e_list)
e_list.remove('twice')
e_list.remove('vero')
print(e_list)

print('banana' in e_list)
print('banana' in b_list)
print(e_list.count('cinnamon'))
e_list.append('cinnamon')
print(e_list.count('cinnamon'))
e_list = "*".join(e_list)
print(e_list)
print(len(e_list))
for elem in e_list:
    print(elem)







