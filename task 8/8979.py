'''(№ 8979) (Апробация-2026) Определите, сколько существует чисел, семеричная запись которых содержит 5 знаков,
из которых ровно одна цифра 0 и не более двух цифр 1.'''

from itertools import *

alf = '0123456'
ans = []
for x in product(alf, repeat=5):
    sl = ''.join(x)
    if sl[0] != '0':
        if sl.count('0') == 1:
            if sl.count('1') <= 2:
                ans.append(sl)
print(ans[10:])
print(len(ans))