'''(№ 2506) В текстовом файле k7.txt находится цепочка из символов латинского алфавита A, B, C длиной
не более 10**6 символов. Найдите длину самой длинной подцепочки, состоящей из символов C.'''

t = open('/home/dmurzin/Downloads/k7.txt').read()
print(t[:100], len(t), set(t))
t1 = t

for x in set(t):
    if x != 'C':
        t = t.replace(x, ' ')
print(t.split())
print(max([(len(x), x) for x in t.split()]))

# regexp
import re

pattern = r'[C]+'
ans = re.findall(pattern, t1)
print(ans)
print(max([(len(x), x) for x in ans]))