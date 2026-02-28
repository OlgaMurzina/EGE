def per(num: int, q: int) -> str:
    # перевод в любую систему счисления 2 <= q <= 36
    alf = '0123456789abcdefghijklmnopqrstuvwxyz'
    # генерация алфавита через ASCII
    alf1 = '0123456789' + ''.join([chr(x) for x in range(ord('a'), ord('z') + 1)])
    print(alf == alf1)
    if num == 0:
        return '0'
    s = ''
    while num > 0:
        s = alf[num % q] + s
        num //= q
    return s

print(type(per(25, 2)))
print(type(bin(25)[2:]))

# для систем счисления с основанием больше 36
def per_(num: int, q: int) -> list:
    if num == 0:
        return [0]
    s = []
    while num > 0:
        s = [num % q] + s
        num //= q
    return s

print(per_(51457, 10000))

def my_int(num: list, q: int) -> int:
    n = num[::-1]
    s = 0
    for i in range(len(n)):
        s += n[i] * q ** i
    return s

print(my_int([5, 1457], 10000))