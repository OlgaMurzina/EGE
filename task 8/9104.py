'''(ЕГЭ-2026) Все шестибуквенные слова, составленные из букв С, О, Л, Н, Ц, Е, записаны в алфавитном порядке
и пронумерованы. Вот начало списка:
1. EEEEEE
2. ЕЕЕЕЕЛ
3. ЕЕЕЕЕН
4. EEEEEO
5. EEEEEC
6. ЕЕЕЕЕЦ
...
Определите, под каким номером в этом списке стоит последнее слово с нечётным номером, которое не начинается с букв Ц
или Н и при этом содержит в своей записи ровно одну букву Ц и ровно одну букву Н.'''

from itertools import *

alf = sorted('СОЛНЦЕ')
ans = []
# k = 1
for k, s in enumerate(product(alf, repeat=6), 1):
    # k += 1
    if k % 2:
        if s[0] not in 'ЦН':
            if s.count('Н') == 1 and s.count('Ц') == 1:
                ans.append((k, s))
print(ans[-1])

ans = []
k = 0
for s in product(alf, repeat=6):
    k += 1
    if k % 2:
        if s[0] not in 'ЦН':
            if s.count('Н') == 1 and s.count('Ц') == 1:
                ans.append((k, s))
print(ans[-1])
