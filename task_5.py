def summa(li):
    cur_sum = 0
    while True:
        list = input('Введите числа через пробел: , q - exit').split()
        for el in list:
            if el == 'exit':
                return cur_sum
            else:
                try:
                    cur_sum += int(el)
                except ValueError:
                    print('Для выхода введите exit')
        print(cur_sum)
print(summa)









