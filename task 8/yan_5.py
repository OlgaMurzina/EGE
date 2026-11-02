"""Определите количество пятизначных шестнадцатеричных чисел, в записи которых ровно одна цифра из набора 0...9."""

from itertools import *

alf = '0123456789abcdef'
ans = []
for s in product(alf, repeat=5):
    if s[0] != '0':
        sl = ''.join(s)
        for x in '0123456789':
            sl = sl.replace(x, '0')
        if sl.count('0') == 1:
            ans.append(s)
print(len(ans))
