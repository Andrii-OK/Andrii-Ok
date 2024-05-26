digit = int(input('введите 5-х значное число:'))

a, b = divmod(digit, 10000)
a1, b1 = divmod(b, 1000)
a2, b2 = divmod(b1, 100)
a3, b3 = divmod(b2, 10)

a,a1,a2,a3,b3=b3,a3,a2,a1,a

print(a,a1,a2,a3,b3)
