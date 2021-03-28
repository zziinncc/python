import time


def s(k, n):
    return ''.join(map(str, range(n + 1))).count(str(k))


def f1(k, n):
    if n < k:
        return 0
    n1 = n
    count = 0
    base = 1
    while n1 > 0:
        m = n1 % 10
        n1 = n1 // 10
        if m == k:
            count += (base * n1 - base * int(k==0) + n - (n1 * 10 * base + m * base) + 1)
        else:
            count += (base * (n1 + int(m > k) - int(k==0 and base > 1)))
        base *= 10
    return count


def f(k, n):
    if n < k:
        return 0
    n1 = n
    count = 0
    base = 1
    while n1 > 0:
        m = n1 % 10
        n1 = n1 // 10

        if m > k:
            count += base * (n1 + 1)
        if m == k:
            count += (base * n1 + n - (n1 * 10 * base + m * base) + 1)
        if m < k:
            count += base * n1
        base *= 10
        if k == 0:
            count -= base // 10
    if k == 0:
        count += 1
    return count


k = 0
n = 0

print(s(k, n), f(k, n), f1(k, n))
