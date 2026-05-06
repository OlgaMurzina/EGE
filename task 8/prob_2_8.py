'''Все восьмибуквенные слова, составленные из букв S, N, E, V, X, I, записаны в алфавитном порядке и
пронумерованы начиная с 1.

Вот начало списка:

EEEEEEEE
EEEEEEEI
EEEEEEEN
EEEEEEES
EEEEEEEV
EEEEEEEX
EEEEEEIE
Сколько слов, которые содержат ровно две гласные, идут в списке раньше, чем слово SIXSEVEN?'''

from itertools import product

alf = sorted('snevxi')
gl = 'ei'
ans = []
k = 0
for x in product(alf, repeat=8):
    sl = ''.join(x)
    a = [x for x in sl if x in gl]
    if len(a) == 2:
        ans.append(sl)
    if sl == 'sixseven':
        break
print(len(ans))

