digit = int(input('введите 5-х значное число:'))

a, b = divmod(digit,10000)
a1, b1 = divmod(b,1000)
a2, b2 = divmod(b1,100)
a3, b3 = divmod(b2,10)

cut1 = (b3*10000+a3*1000+a2*100+a1*10+a*1)



print(cut1)
