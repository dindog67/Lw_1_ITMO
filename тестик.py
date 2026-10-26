f = open('тестик')

ans = [x for x in f]
for i in ans:
    if ' ' in i:
        i = i.replace(' ', '')
        print(i.strip())