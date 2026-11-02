'''	(№ 9111) (ЕГЭ-2026) В файле электронной таблицы 9-291.ods в каждой строке записаны шесть натуральных чисел.
Определите количество строк таблицы, для которых выполнены оба условия:
– в строке только одно число повторяется трижды, остальные числа различны;
– куб повторяющегося числа строки меньше произведения всех её неповторяющихся чисел.
В ответе запишите только число.'''

data1 = open('/home/dmurzin/Downloads/9-291.csv').readlines()
data = []
for st in data1:
    data.append([int(x) for x in st.split()])
print(data[:5])

ans = []
for st in data:
    tr = list(set([x for x in st if st.count(x) == 3]))
    un = [x for x in st if st.count(x) == 1]
    if len(tr) == 1 and len(un) == 3:
        p = 1
        for x in un:
            p *= x
        if tr[0] ** 3 < p:
            ans.append(st)
print(len(ans), ans)




