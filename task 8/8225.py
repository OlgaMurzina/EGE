'''(№ 8225) (О. Лысенков) Сколько существует чисел, двенадцатеричная запись которых содержит 5 знаков
и в которых не более двух раз нечетные цифры стоят рядом?'''

from itertools import *

alf = range(12)
ans = []
alf_odd = range(1, 12, 2)
for s in product(alf, repeat=5):
    if s[0] != 0:
        k = 0
        for i in range(4):
            if s[i] in alf_odd and s[i + 1] in alf_odd:
                k += 1
        if k <= 2:
            ans.append(s)
print(len(ans))

