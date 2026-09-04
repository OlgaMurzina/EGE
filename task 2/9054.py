'''(№ 9054) (ЕГЭ-2026) Логическая функция F задаётся выражением
¬(z → x) ∨ (y → w) ∨ ¬y
На рисунке приведён частично заполненный фрагмент таблицы истинности функции F, содержащий неповторяющиеся
строки. Определите, какому столбцу таблицы истинности функции F соответствует каждая из переменных x, y, z, w.
В ответе напишите буквы x, y, z, w в том порядке, в котором идут соответствующие им столбцы. Буквы в ответе
пишите подряд, никаких разделителей между буквами ставить не нужно.'''

from itertools import product, permutations

# print('x y z w')
# for x, y, z, w in product([0,1], repeat=4):
#     f = (not(z <= x)) or (y <= w) or (not(y))
#     if f == 0:
#         print(x, y, z, w)

def v(x, y, z, w):
    return (not(z <= x)) or (y <= w) or (not(y))

for a, b, c, d, e, f, g in product([0, 1], repeat=7):
    t = ((0, 1, a, b),
         (c, 0, d, e),
         (1, f, 0, g))
    if len(set(t)) == 3:
        for p in permutations('xyzw'):
            if all(v(**dict(zip(p, r))) == 0 for r in t):
                print(*p, sep='')