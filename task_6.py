
with open(r'task6.txt', 'r', encoding='UTF-8') as f:
    print(f.read())
    for line in f:
        # 'Информатика', 'л', 'пр', 'лаб' = line.split()
        dict = {'x': 'л', 'y': 'пр', 'z': 'лаб'}
        # sum = int('л') + int('пр') + int('лаб')
        a = f.readline(sum(x + y + z))
        b = f.readline(sum(x + y + z))
        c = f.readline(sum(x + y + z))
    print(f'Информатика - {a}\n,Физика -  {b}\n, Физкультура - {c}\n')

