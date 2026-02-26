'''(№ 8582) (ЕГКР-2025) В файле электронной таблицы 9-263.ods в каждой строке записаны семь целых чисел.
Определите количество строк таблицы, для которых выполнены оба условия:
– в строке есть одно число, которое повторяется трижды, остальные четыре числа различны;
– максимальное число строки не повторяется.
В ответе запишите только число.'''

data1 = open('/home/dmurzin/Downloads/9-263.csv').readlines()
data = []
for st in data1:
    s = [int(x) for x in st.split(';')]
    data.append(s)
# print(data[:20])

ans = []
for i in range(len(data)):
    st = data[i]
    tr = [x for x in st if st.count(x) == 3]
    un = [x for x in st if st.count(x) == 1]
    if len(tr) == 3 and len(un) == 4:
        if max(st) in un:
            ans.append(st)
print(len(ans))