
with open(r'tsk5.txt', 'w', encoding='UTF-8') as f:
    print(f.write(f'{[5, 12, 3, 27]}'))
    # f.seek(0)
    s = sum([5, 12, 3, 27])
    print(s)
    f.write(f'\nСумма чисел: 47')
