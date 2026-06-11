'''(№ 8948) Текстовый файл 24-378.txt содержит только заглавные буквы латинского алфавита и десятичные цифры.
Найдите минимальное количество идущих подряд символов, среди которых есть все цифры и есть ровно три буквы
латинского алфавита от A до F (других букв может быть сколько угодно). В ответе запишите число – количество
символов в найденной последовательности.'''

t = open('/home/dmurzin/Downloads/24-378.txt').read()
print(t[:100], len(t))

#
ans = []
i = 0
af = 1 if t[i] in 'ABCDEF' else 0
dig = [0] * 10
if t[i] in '0123456789':
    dig[int(t[i])] += 1
s = t[i] if t[i] in '0123456789ABCDEF' else ''
j = i + 1
while i < len(t) - 2:
    while j < len(t) - 1 and t[j] in '0123456789ABCDEF' and af < 4 and not all(x > 0 for x in dig):
        if t[j] in 'ABCDEF':
            af += 1
        else:
            dig[int(t[j])] += 1
        s += t[j]
        j += 1
        # print(s, af, dig)
    if af == 3 and all(x > 0 for x in dig):
        ans.append((len(s), s))
        if s[0] in '0123456789':
            dig[int(s[0])] -= 1
        elif s[0] in 'ABCDEF':
            af -= 1
        s = s[1:]
        i += 1
        print(ans)
    else:
        i = j + 1
        af = 1 if t[i] in 'ABCDEF' else 0
        dig = [0] * 10
        if t[i] in '0123456789':
            dig[int(t[i])] += 1
        s = t[i] if t[i] in '0123456789ABCDEF' else ''
        j = i + 1
    # print(s, af, dig, i, j)
print(min(ans))








# разбивка на слова тоже не работает - нужно брать еще и подпоследовательности
t1 = t
alf = 'ghijklmnopqrstuwvxyz'.upper()
for x in set(alf):
    t1 = t1.replace(x, ' ')
ans1 = [x for x in t1.split() if len(x) > 13]
# print(ans)
ans2 = []
for x in ans1:
    a = [y for y in x if y in '0123456789']
    b = [y for y in x if y in 'ABCDEF']
    if len(set(a)) == 10 and len(b) == 3:
        ans2.append((len(x), x))
ans = []
minn = 10 ** 3
p = None
for x in ans2:
    s = x[1]
    l = 0
    r = len(s)
    while l < r:
        st = s[l:r]
        a = [y for y in st if y in '0123456789']
        b = [y for y in st if y in 'ABCDEF']
        if len(set(a)) == 10 and len(b) == 3:
            ans.append((len(st), st))
            r -= 1
        else:
            l += 1
            r = len(s)
print(min(ans))

print()
'''
# regexp не работает тут, т.к. режет на неперескающиеся куски всю строку
import re
pattern = r'(?:[0-9A-F]){12,}'
ans = re.findall(pattern, t)
# print(ans)
for x in ans:
    a = [y for y in x if y in '0123456789']
    b = [y for y in x if y in 'ABCDEF']
    if len(set(a)) == 10 and len(b) == 3:
        print(len(x), x)
'''