'''Определите количество строк таблицы, для которых выполнены оба условия:
в строке есть числа, кратные трём
сумма двух наименьших чисел больше второго по величине числа
В ответе запишите только число.'''

data1 = open('9__2.csv').readlines()
data = []
for st in data1:
    s = [int(x) for x in st.split(';')]
    data.append(s)
# print(data)

ans = []
for i in range(len(data)):
    st = sorted(data[i])
    s3 = [x for x in st if x % 3 == 0]
    if len(s3) > 0:
        if st[0] + st[1] > sorted(set(st))[-2]:
            ans.append(st)
print(len(ans))
# print(ans)