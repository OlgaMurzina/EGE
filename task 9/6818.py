'''(№ 6818) (ЕГЭ-2023) В файле электронной таблицы 9-226.xls в каждой строке записаны семь натуральных чисел.
Определите сумму чисел в строке таблицы с наименьшим номером, для которой выполнены оба условия:
– в строке есть два числа, которые повторяются дважды, остальные три числа различны;
– максимальное число строки не повторяется.
В ответе запишите только число.'''

data1 = open('/home/dmurzin/Downloads/9-226.csv').readlines()
data = []
for st in data1:
    s = [int(x) for x in st.split(';')]
    data.append(s)
# print(data)
ans = []
for i in range(len(data)):
    st = data[i]
    dbl = [x for x in st if st.count(x) == 2]
    un = [x for x in st if st.count(x) == 1]
    if len(dbl) == 4 and len(un) == 3:
        if max(st) in un:
            ans.append((i + 1, st))
print(ans)
print(sum(min(ans)[1]))
