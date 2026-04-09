'''(№ 2850) Рассматриваются целые числа, принадлежащих числовому отрезку [356738; 404321],
которые представляют собой произведение двух различных простых делителей.
В ответе запишите количество таких чисел и такое из них, простые делители которого
отличаются друг от друга больше всего.'''


def isprime(x):
    # проверка на простые числа
    for d in range(2, round(x ** 0.5) + 1):
        if x % d == 0:
            return False
    return True


def good(x):
    # поиск всех делителей числа
    de = []
    for d in range(2, round(x ** 0.5) + 1):
        if x % d == 0:
            if isprime(d) and isprime(x // d):
                de.append(d)
                if x // d not in de:
                    de.append(x // d)
    if len(de) == 2:
        de = sorted(de)
        return de
    return []


k = 0
maxx = -10 ** 10
num = None
for x in range(356738, 404322):
    y = good(x)
    if y:
        k += 1
        if y[-1] - y[0] > maxx:
            maxx = y[-1] - y[0]
            num = x
print(k, num, good(num))
