
a = int(input('Введите результат в км за 1 день: '))
print(a)
b = int(input('Введите общий результат: '))
print(b)
s = a
days = 1
print(days, s)
while s < b:
    days += 1
    s *= 1.1
    print(days, s)






