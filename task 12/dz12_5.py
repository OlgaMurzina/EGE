
from itertools import *
'''
alf = '01'
ans = []
for x in product(alf, repeat=10):
    xx = [' '] + list(x) + [' ']
    st = xx.copy()
    i = 0
    q = 0
    while True:
        if q == 0:
            if xx[i] == ' ':
                i += 1
                q = 1
        elif q == 1:
            if xx[i] == ' ':
                break
            elif xx[i] == '1':
                xx[i] = '0'
                i += 1
                q = 1
            elif xx[i] == '0':
                xx[i] = '1'
                i += 1
                q = 2
        elif q == 2:
            if xx[i] == ' ':
                break
            elif xx[i] == '1':
                xx[i] = '1'
                i += 1
                q = 2
            elif xx[i] == '0':
                xx[i] = '0'
                i += 1
                q = 1
    if st.count('1') == 4:
        ans.append((xx.count('1'), st, xx))
print(sorted(ans)[::-1][:5])
'''
xx = [' '] + ['0'] + ['1'] * 200 + ['0'] * 299 + [' ']
q = 0
i = 0
while True:
    if q == 0:
        if xx[i] == ' ':
            i += 1
            q = 1
    elif q == 1:
        if xx[i] == ' ':
            break
        elif xx[i] == '1':
            xx[i] = '0'
            i += 1
            q = 1
        elif xx[i] == '0':
            xx[i] = '1'
            i += 1
            q = 2
    elif q == 2:
        if xx[i] == ' ':
            break
        elif xx[i] == '1':
            xx[i] = '1'
            i += 1
            q = 2
        elif xx[i] == '0':
            xx[i] = '0'
            i += 1
            q = 1

print(xx.count('1'))