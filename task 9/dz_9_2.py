'''
Откройте файл электронной таблицы, в каждой строке которой — четыре натуральных числа. Определите количество строк таблицы,
для которых выполнены оба условия:
в строке есть числа, кратные трём
сумма двух наименьших чисел больше второго по величине числа
В ответе запишите только число.
'''

data1 = open("9_2.csv").readlines()
data = []
for st in data1:
    s = [int(x) for x in st.split(";")]
    data.append(s)
ans = []
for i in range(len(data)):
    s = data[i]
    n = 0
    for z in range(len(s)):
        if s[z] % 3 == 0:
            n += 1
    if n >= 1:
        m = sorted(s)
        k = sorted(set(s))
        if m[0] + m[1] > k[-2]:
            ans.append(s)
print(len(ans))