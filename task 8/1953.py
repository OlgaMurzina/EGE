'''(№ 1953) Петя составляет шестибуквенные слова перестановкой букв слова КАБАЛА. При этом он избегает
слов с двумя подряд одинаковыми буквами. Сколько всего различных слов может составить Петя?'''

from itertools import permutations

alf = 'КАБАЛА'
ans = []
for s in permutations(alf):
    for i in range(5):
        if s[i] == s[i + 1]:
            break
    else:
        ans.append(s)
print(len(ans), len(set(ans)))

ans = []
for a in range(6):
    for b in range(6):
        for c in range(6):
            for d in range(6):
                for e in range(6):
                    for f in range(6):
                        ind = [a, b, c, d, e, f]
                        if len(ind) == len(set(ind)):
                            s = alf[a] + alf[b] + alf[c] + alf[d] + alf[e] + alf[f]
                            for i in range(5):
                                if s[i] == s[i + 1]:
                                    break
                            else:
                                ans.append(s)
print(len(set(ans)))
