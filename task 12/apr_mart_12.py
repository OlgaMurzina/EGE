s = list(' ' + bin(800)[2:] + ' ')
print(s)
q = 0
i = len(s) - 1
print(len(s), i)
while True:
    if q == 0:
        if s[i] == ' ':
            i -= 1
            q = 1
    elif q == 1:
        if s[i] == ' ':
            i += 1
            q = 2
        elif s[i] == '0':
            s[i] = '0'
            i -= 1
            q = 1
        elif s[i] == '1':
            s[i] = '1'
            i -= 1
            q = 1
    elif q == 2:
        if s[i] == '0':
            s[i] = '0'
            i -= 1
            q = 2
        elif s[i] == '1':
            s[i] = '1'
            i += 1
            q = 3
    elif q == 3:
        if s[i] == ' ':
            i += 1
            q = 4
        elif s[i] == '0':
            s[i] = '0'
            i += 1
            q = 3
        elif s[i] == '1':
            s[i] = '0'
            i += 1
            q = 4
    elif q == 4:
        if s[i] == ' ':
            break
        elif s[i] == '0':
            s[i] = '0'
            i += 1
            q = 4
        elif s[i] == '1':
            s[i] = '1'
            i += 1
            q = 4
r = ''.join(s)
print(r, int(r, 2))
