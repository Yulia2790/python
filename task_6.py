from itertools import count, cycle

for i in count(3, 1):
    print(i)
    if i > 9:
        break

k = 0
for elem in cycle(['budget', 'salary', 'tax', 'total']):
    print(elem)
    k += 1
    if k > 20:
        break