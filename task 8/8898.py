'''(№ 8898) Сколько существует чисел, четырнадцатеричная запись которых содержит пять цифр, среди которых
есть только две чётные цифры, причём они равны между собой и между ними стоит только одна цифра.'''

from itertools import *

alf = '0123456789abcd'

k = 0
for s in product(alf, repeat=5):
    if s[0] != '0':
        sl = ''.join(s)
        a = [x for x in sl if int(x, 14) % 2 == 0]
        if len(a) == 2 and a[0] == a[1]:
            for i in range(len(sl) - 2):
                if sl[i] == a[0] and sl[i + 1] != a[0] and sl[i + 2] == a[0]:
                    print(sl)
                    k += 1
print(k)
