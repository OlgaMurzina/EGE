'''(№ 8901) В файле электронной таблицы 9-277.ods в каждой строке записаны семь целых чисел. Определите сумму
 нечётных номеров строк, для которых выполнены оба условия:
– одно из чисел строки точно равно среднему арифметическому всех элементов строки;
– строка содержит квадрат натурального числа.
В ответе запишите только число.'''

data1 = open('9-277.csv').readlines()
print(data1[:5])
data = []
for s in data1:
    data.append([int(x) for x in s.split(';')])
print(data[:5])

kv = [x ** 2 for x in range(1, 1000)]
ans = []
k = 0
for s in data:
    k += 1
    s = sorted(s)
    if k % 2:
        a = []
        for x in s[2:-2]:
            if x == sum(s) / 7:
                a.append(x)
        if len(a) == 1:
            b = [x for x in s if x in kv]
            # print(s, a, b)
            if len(b) >= 1:
                ans.append(k)
print(sum(ans))

