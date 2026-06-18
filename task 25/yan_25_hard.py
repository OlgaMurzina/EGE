'''Рассматриваются целые числа, принадлежащих числовому отрезку [485617; 529678], которые представляют собой
произведение трёх различных простых делителей, оканчивающихся на одну и ту же цифру.
В качестве ответа приведите все числа, разность максимального и минимального простых делителей которого меньше 100.
Для каждого такого числа сначала запишите само число, а затем разность максимального и минимального простых делителей'''

def delit(n):
    de = []
    for d1 in range(2, round(n ** 0.5) + 1):
        if n % d1 == 0:
            if prost(d1):
                y = prost2(n // d1)
                if y:
                    d2, d3 = y
                    if len(set([d1, d2, d3])) == 3:
                        if str(d1)[-1] == str(d2)[-1] == str(d3)[-1]:
                            if max(d1, d2, d3) - min(d1, d2, d3) < 100:
                                return (max(d1, d2, d3) - min(d1, d2, d3))
    return 0

def prost(n):
    for d in range(2, round(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True

def prost2(n):
    de = []
    for d in range(2, round(n ** 0.5) + 1):
        if n % d == 0:
            if prost(d):
                if prost(n // d) and n // d != d:
                    de.append(d)
                    de.append(n // d)
    if de:
        return de
    return 0

for x in range(485617, 529679):
    y = delit(x)
    if y:
        print(x, y)