z = input("Действие (+,*,- или /);")
x = float(input('x = '))
y = float(input('y = '))
if z == '+':
     print(x + y)
elif z == '-':
     print(x - y)
elif z == '*':
     print(x * y)
elif z == '/':
    if y != 0:
     print(x / y)
    else:
     print('деление на ноль!')

