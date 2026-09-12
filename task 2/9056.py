'''(№ 9056) (ЕГЭ-2026) Логическая функция F задаётся выражением (z → ¬(y → x)) ∨ w
На рисунке приведён частично заполненный фрагмент таблицы истинности функции F, содержащий неповторяющиеся строки.
Определите, какому столбцу таблицы истинности функции F соответствует каждая из переменных x, y, z, w.'''

from itertools import *

def v(x, y, z, w):
    return (z <= (not(y <= x))) or w

for a, b, c, d, e, f, g in product([0, 1], repeat=7):
    t = ((a, 1, b, c),
         (d, e, 0, 0),
         (f, 0, 1, g))
    if len(set(t)) == 3:
        for p in permutations('xyzw'):
            if all(v(**dict(zip(p, r))) == 0 for r in t):
                print(''.join(p))