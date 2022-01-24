
f = open(r'test2.txt', 'r')
for text in f:
    print(text)
    quantity = f.readlines()
    print('Количество строк:', len(quantity))
    text = f.read()
    q_word = text.split()
    print('Количество слов:', len(q_word))

f.close()
