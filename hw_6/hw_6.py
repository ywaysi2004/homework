print('and:')
print(False and False); print (False and True)
print(True and False); print (True and True); print()
print('or:')
print(False or False); print (False or True)
print(True or False); print (True or True); print()
print('not:')
print(not False); print (not True); print()
# Логічні вирази
a = True;b= False; c = True
f = a and not b or c or (a and (b or c))
print (f)

a = 2; b = 5                #менше
print(b > 3)                #більше
print(a <= 2)               #менше або дорівнює
print(b >= 7)               #більше або дорівнює
print(a < 3 < b)            #подвійне порівняння
print(a == b)               #рівність
print(a != b)               #нерівність
print(a is b)               #ідентичність об'єктів в пам'яті
print(a is not b)           #a і b - різні об'єкти
#(хоча їхні значенння можуть бути однаковими - ріними)