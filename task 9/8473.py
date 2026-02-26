'''(№ 8473) (К. Багдасарян) В файле электронной таблицы 9-259.xls в каждой строке записаны шесть целых чисел.
Определите количество строк таблицы, для которой выполнены оба условия:
– в строке имеются числа, оканчивающиеся на 3;
– шесть чисел строки после перестановки могут образовать арифметическую прогрессию.
В ответе запишите только число.'''

data1 = open('/home/dmurzin/Downloads/9-259.csv').readlines()
data = []
for st in data1:
    s = [int(x) for x in st.split(';')]
    data.append(s)
# print(data)

ans = []
for i in range(len(data)):
    st = sorted(data[i])
    s3 = [x for x in st if abs(x) % 10 == 3]
    if len(s3) > 0:
        if st[1] - st[0] == st[2] - st[1] == st[3] - st[2] == st[4] - st[3] == st[5] - st[4]:
            ans.append(st)
print(len(ans))
print(ans)