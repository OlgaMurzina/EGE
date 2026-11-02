'''(№ 8579) Сколько существует чисел, пятнадцатеричная запись которых содержит шесть цифр,
причем среди них по крайней мере одна цифра 0 и ровно две цифры с числовым значением, превышающим 12,
причём стоящие рядом.'''

from itertools import product

alf = range(15)
ans = []
for s in product(alf, repeat=6):
    if s[0] != 0:
        if s.count(0) >= 1:
            dv = [x for x in s if x > 12]
            if len(dv) == 2:
                for i in range(5):
                    if s[i] > 12 and s[i + 1] > 12:
                        ans.append(s)
print(len(ans))