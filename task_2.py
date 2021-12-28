print('Hello 2')

time = input('seconds: ') #seconds = '10000'
time = int(time)
print(type(time))

s = (time % 60)
print(s)
m = (time // 60 % 60)
print(m)
h = (time // 3600)
print(h)
print((time // 3600), ":", (time // 60 % 60), ":", (time % 60))


