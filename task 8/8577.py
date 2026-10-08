"""Сколько существует чисел, пятнадцатеричная запись которых содержит четыре цифры, причём среди них
ровно две цифры 5 и никакие две одинаковые цифры не стоят рядом?"""

from itertools import *

alf = range(15)

ans = []
for s in product(alf, repeat=4):
    if s[0] != 0:
        if s.count(5) == 2:
            for i in range(3):
                if s[i] == s[i + 1]:
                    break
            else:
                ans.append(s)
print(len(ans))

ans = []
for a in list(alf)[1:]:
    for b in alf:
        for c in alf:
            for d in alf:
                s = (a, b, c, d)
                if s.count(5) == 2:
                    f = 1
                    for i in range(3):
                        if s[i] == s[i + 1]:
                            f = 0
                            break
                    if f:
                        ans += [s]
print(len(ans))
