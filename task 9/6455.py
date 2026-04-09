'''(№ 6455) В файле электронной таблицы 9-210.xls в каждой строке записаны 6 натуральных чисел. Определите
количество строк таблицы, содержащих числа, для которых выполнены следующие условия:
– минимальное число не повторяется;
– среди остальных чисел строки есть повторяющиеся;
– сумма максимального и минимального чисел строки меньше, чем сумма повторяющихся чисел.'''

data1 = open('/home/dmurzin/Downloads/9-210.csv').readlines()
data = []
for st in data1:
    data.append([int(x) for x in st.split(';')])
print(data[:5])

ans = []
for st in data:
    a = sorted(st)
    if st.count(a[0]) == 1:
        b = [x for x in a[1:] if a[1:].count(x) > 1]
        if len(b) > 0:
            if a[0] + a[-1] < sum(b):
                ans.append(st)
print(len(ans))
