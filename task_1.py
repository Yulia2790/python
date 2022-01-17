
def func(a, b):
    try:
        res = a / b
        print(res)
    except ZeroDivisionError:
        return print('Error')
func(int(input('Введите число a: ')), int(input('Введите число b: ')))






