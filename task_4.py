
with open(r'4.txt', 'r') as f:
    print(f.read())
    f.seek(0)
    for text in f:
        a = text.replace('Один', 'Два')
        b = text.replace('Two','Два')
        c = text.replace('Three','Три')
        d = text.replace('Four','Четыре')
        # new_text = [a, b, c, d]
        print(a, b, c, d)
with open(r'4_new.txt', 'w') as f:
    f.write(a, b, c, d)