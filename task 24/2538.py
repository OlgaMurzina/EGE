'''(№ 2537) (К. Амеличев) Текстовый файл 24-5.txt содержит последовательность из символов «(»и «)»,
всего не более 10**6 символов. Определите количество пар скобок «()» в этом файле.
Определите максимальное количество подряд идущих пар скобок «()» в этом файле'''

t = open('/home/dmurzin/Downloads/24-5.txt').read()
print(t[:1000])

ans = []
j = t.index('()')
s = ''
for i in range(j, len(t) - 2, 2):
    if t[i: i + 2] == '()':
        s += t[i:i + 2]
    else:
        if s:
            ans.append((len(s), s))
        s = ''
    # print(s)
ans.append((len(s), s))
print(max(ans))

# regexp
import re
pattern = r'((\(\))\2+)'
ans = re.findall(pattern, t)
print(max((len(x[0]), x[0]) for x in ans))