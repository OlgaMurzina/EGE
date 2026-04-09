'''(№ 5650) (М. Ишимов) В файле электронной таблицы 9-176.xls в каждой строке содержатся семь натуральных чисел.
Определите количество строк таблицы, для которых выполнены оба условия:
– в строке есть хотя бы одно повторяющееся число;
– сумма неповторяющихся чисел строки нечётная.'''

data1 = open('/home/dmurzin/Downloads/9-176.csv').readlines()
data = []
for st in data1:
    data.append([int(x) for x in st.split(';')])
print(data)

ans = []
for st in data:
    # в строке есть хотя бы одно повторяющееся число
    a = [x for x in st if st.count(x) > 1]
    b = [x for x in st if st.count(x) == 1]
    if len(a) > 0:
        if sum(b) % 2 == 1:
            ans.append(st)
print(len(ans))

