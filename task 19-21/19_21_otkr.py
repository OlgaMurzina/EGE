def f(x1, x2, c, win):
    if x1 + x2 >= 154:
        return c in win
    elif c > max(win):
        return 0
    moves = [f(x1 + 4, x2, c + 1, win), f(x1, x2 + 4, c + 1, win),
             f(x1 * 3, x2, c + 1, win), f(x1, x2 * 3, c + 1, win)]
    if c % 2 != max(win) % 2:
        return any(moves)
    return all(moves)

def g(x1, x2, c, win):
    if x1 + x2 >= 154:
        return c in win
    elif c > max(win):
        return 0
    moves = [g(x1 + 4, x2, c + 1, win), g(x1, x2 + 4, c + 1, win),
             g(x1 * 3, x2, c + 1, win), g(x1, x2 * 3, c + 1, win)]
    if c % 2 != max(win) % 2:
        return any(moves)
    return any(moves)

# 19 неоптим
for s in range(1, 143):
    if g(11, s, 0, [2]) == 1:
        print('19)', s)
        break

# 20 оптим
for s in range(1, 143):
    if f(11, s, 0, [3]) == 1:
        print('20)', s)

# 21 оптим
for s in range(1, 143):
    if f(11, s, 0, [2, 4]) == 1 and f(11, s, 0, [2]) == 0:
        print('21)', s)