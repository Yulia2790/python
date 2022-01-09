
list = input('Введите список: ').split()
print(list)
print(len(list))
list[0], list[1] = list[1], list[0]
list[2], list[3] = list[3], list[2]
list[4], list[5] = list[5], list[4]
print(list)






#list2 = [22, True, 14.45, 'asd']
#print(list2)
#print(len(list2))