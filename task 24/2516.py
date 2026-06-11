'''(№ 2516) (А.М. Кабанов) В текстовом файле k7a-2.txt находится цепочка из символов латинского алфавита
A, B, C, D, E, F. Найдите длину самой длинной подцепочки, состоящей из символов A, C, D (в произвольном порядке).'''

t = open('/home/dmurzin/Downloads/k7a-2.txt').read()
print(t[:100], len(t), set(t))

for x in 'BEF':
    t = t.replace(x, ' ')
ans = [(len(x), x) for x in t.split()]
print(max(ans))
for x in ans:
    if x[0] == 11:
        print(x)

# regexp
import re
pattern = r'[ACD]+'
ans = re.findall(pattern, t)
print(max([(len(x), x) for x in ans]))