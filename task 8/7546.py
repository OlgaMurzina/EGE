'''(№ 7546) (ЕГЭ-2024) Определите количество 14-ричных пятизначных чисел, в записи которых ровно одна цифра 9
и не более трех цифр с числовым значением, превышающим 10.'''

# alf
alf = '0123456789abcd'   # 14-рич система
ans = []
# перебор - механика
for d1 in alf[1:]:   # для создания чисел исключить 0!!!!
    for d2 in alf:
        for d3 in alf:
            for d4 in alf:
                for d5 in alf:
                    # клеим слово
                    sl = d1 + d2 + d3 + d4 + d5
                    # проверяем условия из задачи
                    if sl.count('9') == 1:   # одна цифра 9
                        a = [x for x in sl if x in alf[-3:]]
                        if len(a) <= 3:   # не более трех цифр с числовым значением, превышающим 10
                            ans.append(sl)
print(len(ans))

# автомат
from itertools import product

res = []
for x in product(alf, repeat=5):
    sl = ''.join(x)
    if sl[0] != '0':
        if sl.count('9') == 1:   # одна цифра 9
            a = [x for x in sl if x in alf[-3:]]
            if len(a) <= 3:   # не более трех цифр с числовым значением, превышающим 10
                res.append(sl)
print(len(res))