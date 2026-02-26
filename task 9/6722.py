'''(№ 6722) (ЕГЭ-2023) В файле электронной таблицы 9-222.xls в каждой строке записаны шесть натуральных чисел.
Определите наименьший номер строки таблицы, для чисел которой выполнены оба условия:
– в строке есть только одно число, которое повторяется дважды, остальные четыре числа различны;
– повторяющееся число строки не меньше, чем среднее арифметическое четырёх её неповторяющихся чисел.
В ответе запишите только число.'''

# чтение данных из файла .csv
data1 = open('/home/dmurzin/Downloads/9-222.csv').readlines()
data = []
for st in data1:
    s = [int(x) for x in st.split(';')]
    data.append(s)
# print(data[:10])

# обработка
ans = []
for i in range(len(data)):
    st = data[i]
    double = [x for x in st if st.count(x) == 2]
    uniq = [x for x in st if st.count(x) == 1]
    # print(st, double, uniq)
    if len(double) == 2 and len(uniq) == 4:
        avg = sum(uniq) / 4
        if double[0] >= avg:
            ans.append((i + 1, st))

print(max(ans))
print(ans)

