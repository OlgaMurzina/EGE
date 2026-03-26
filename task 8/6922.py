'''(№ 6922) (Е. Джобс) Григорий составляет буквенные последовательности путем перестановки букв слова НОСОЧЕЧКИ.
Сколько Григорий может составить различных последовательностей, в которых гласные и согласные буквы чередуются?'''

from itertools import *

alf = 'НОСОЧЕЧКИ'
gl = 'ОЕИ'
sgl = 'НСЧК'

ans = []
for s in permutations(alf):
    sl = ''.join(s)
    f = 1
    for i in range(len(sl) - 1):
        if (sl[i] in gl and sl[i + 1] in gl) or (sl[i] in sgl and sl[i + 1] in sgl):
            f = 0
            break
    if f:
        if sl not in ans:
            ans.append(sl)
print(len(ans))


