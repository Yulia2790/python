
dict = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
month = int(input('Число месяца: '))
for elem in dict:
    if month in dict[elem]:
        print(elem)




list = ['зима', 'весна', 'лето', 'осень']
m = int(input('Число месяца: '))
n = (m // 3) % 4
for elem in list:
    if n == 0:
        print('зима')
    if n == 1:
        print('весна')
    if n == 2:
        print('лето')
    if n == 3:
        print('осень')
    break















