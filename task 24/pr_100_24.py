# 9751490

def calc(b):
    bb = '0o'
    for i in range(len(b)):
        if b[i] in '+*':
            bb += b[i] + '0o'
        else:
            bb += b[i]
    return eval(bb)

import re

t = open('24-314.txt').read().strip()
tt = t.split('F')
mask = r'(?:[1-7][0-7]*[\+\*])+'
ans = []
for x in tt:
    s = x
    while len(s) > 0 and not re.match(mask, s):
        s = s[:-1]
    if len(s) > 0:
        ss = re.match(mask, s).group()[:-1]
        ans.append((len(ss), ss))
print(*sorted(ans, reverse=True)[:10], sep='\n')
print()
print(max(ans))
# print(*[x for x in ans if x[0] == max(ans)[0]])
# calc
print(calc(max(ans)[1]))
print()
# вообще самая большая подстрока в 8-рич системе
answ = [(len(x[:-1]), x[:-1]) for x in re.findall(mask, t)]
print(max(answ))
print(calc(max(answ)[1]))


