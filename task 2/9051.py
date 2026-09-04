'''(№ 9051) (Открытый вариант-2026) Логическая функция F задаётся выражением
((z → x) → (x ≡ y)) ∨ ¬w
На рисунке приведён частично заполненный фрагмент таблицы истинности функции F,
содержащий неповторяющиеся строки. Определите, какому столбцу таблицы истинности функции
F соответствует каждая из переменных x, y, z, w.'''

from itertools import product, permutations

def f(x, y, z, w):
    return ((z <= x) <= (x == y)) or (not(w))

for a, b, c, d, e in product([0, 1], repeat=5):
    t = (
    (a, 0, 1, 0),
    (0, b, c, 0),
    (d, 1, 1, e)
    )
    if len(set(t)) == 3:
        for p in permutations('xyzw'):
            if all(f(**dict(zip(p, r))) == 0 for r in t):
                print(*p)
                print(t)

