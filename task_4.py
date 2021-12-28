
s = int(input('Number: '))
print(s)
b = 0
while s > 0:
     c = s % 10
     s = s // 10
     if c > b:
         b = c
print(b)
print('the largest number is', b)




#print('the largest number is', b)



















