def f(n, k12):
    if n == 3:
        if k12 == 12:
            return 1
        else:
            return 0
    elif n < 3 or n == 9:
        return 0
    elif n == 12:
        return f(n - 1, 12) + f(n - 3, 12) + f(n // 2, 12)
    else:
        return f(n - 1, k12) + f(n - 3, k12) + f(n // 2, k12)

print(f(19, 0))