digit = int(input('введите 4-х значное число:'))

a, b = divmod(digit, 1000)
a1, b1 = divmod(b, 100)
a2, b2 = divmod(b1, 10)

print(a)
print(a1)
print(a2)
print(b2)