'''Найдите первые пять чисел, больших 500 000, сумма делителей которых соответствует маске *7?. Найденные числа
выведите в порядке возрастания, справа от каждого запишите найденную сумму делителей.'''

def good(x):
    de = [1, x]
    for d in range(2, round(x ** 0.5) + 1):
        if x % d == 0:
            de.append(d)
            if x // d not in de:
                de.append(x // d)
    return sum(de)


from fnmatch import fnmatch

mask = '*7?'
k = 0
for x in range(500_001, 10 ** 6):
    y = good(x)
    if y and fnmatch(str(y), mask):
        k += 1
        print(x, y)
        if k == 5:
            break
