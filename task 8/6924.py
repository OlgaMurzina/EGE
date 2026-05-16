'''(№ 6924) (Е. Джобс) Петя составляет 7-буквенные кодовые слова из букв В, Е, Б, И, Н, А, Р. Каждую букву нужно
использовать ровно 1 раз, при этом нельзя ставить подряд две гласные или две согласные. Сколько различных кодовых слов
может составить Петя?'''

from itertools import *

alf = 'ВЕБИНАР'
gl = 'ЕИА'
sgl = 'ВБНР'
ans = []
for x in permutations(alf):
    sl = ''.join(x)
    f = 1
    for i in range(6):
        if (sl[i] in gl and sl[i + 1] in gl) or (sl[i] in sgl and sl[i + 1] in sgl):
            f = 0
            break
    if f == 1:
        ans.append(sl)
print(len(set(ans)))

