
f = open('3.txt', 'r')
lastname = []
salary = []
f = f.read().split('\n')
for line in f:
    line = line.split()
    if int(line[1]) < 20000:
        lastname.append(line[0])
    salary.append(line[1])
s_salary = sum(salary) / len(salary)
print(f'{lastname}: зарплата меньше 20000',{s_salary}: средний оклад')

f.close()