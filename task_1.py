
f = open('test1.txt', 'w')
line = input('Введите строки \n')
while line:
    f.writelines(line)
    line = input('Введите строки \n')
    if not line:
        break
f.close()
