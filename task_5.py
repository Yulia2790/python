from functools import reduce

new = [i for i in range(100, 1001) if i % 2 == 0]
print(new)

def func(prev_el, el):
    return prev_el * el
print(reduce(func, new))