'''(№ 7465) (ЕГЭ-2024) В файле электронной таблицы 9-244.xls в каждой строке записаны четыре натуральных числа.
Определите количество строк таблицы, для которых выполнены оба условия:
– наибольшее из четырёх чисел меньше суммы трёх других;
– среди четырёх чисел есть только одна пара равных чисел.
В ответе запишите только число.'''

data1 = open('/home/dmurzin/Downloads/9-244.csv').readlines()
data = []
for st in data1:
    s = [int(x) for x in st.split(';')]
    data.append(s)
# print(data)

ans = []
for i in range(len(data)):
    st = sorted(data[i])
    if st[-1] < sum(st[:-1]):
        dv = [x for x in st if st.count(x) == 2]
        if len(dv) == 2:
            ans.append(st)
print(len(ans))
