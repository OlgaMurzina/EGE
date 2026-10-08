'''(№ 5969) (А. Богданов) Логическая функция F задаётся выражением x → ((w → y) ≠ z).
На рисунке приведён частично заполненный фрагмент таблицы истинности функции F, содержащий неповторяющиеся строки.
Определите, какому столбцу таблицы истинности функции F соответствует каждая из переменных x, y, z, w.'''

from itertools import *

def v(x, y, z, w):
    return x <= ((w <= y) != z)

for a,b,c,d,e in product([0, 1], repeat=5):
    t = ((a, 1,1,1,1),
         (0,0,b,c,0),
         (d,0,e,0,0))
    if len(set(t)) == 3:
        for p in permutations('xyzw'):
            if all(v(**dict(zip(p, r))) == r[-1] for r in t):
                print(''.join(p))
print()

# ((1≡w)≡(¬((w∧x)∨y)))→z
from itertools import *

def n(x, y, z, w):
    return ((1 == w) == (not ((w and x) or y))) <= z

ans = []
for a, b, c, d, e, f, g, h, i, j in product([0, 1], repeat=10):
    s = ((a, b, 1, c, 0),
         (1, d, 1, e, 0),
         (0, 1, 0, 0, 1),
         (1, f, 1, g, 1),
         (h, i, 1, j, 1))
    if len(set(s)) == len(s):
        for p in permutations('xyzw'):
            if all(n(**dict(zip(p, r))) == r[-1] for r in s):
                ans.append(p)

print(ans)