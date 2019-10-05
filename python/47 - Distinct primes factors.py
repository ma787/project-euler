def prime_factors(n):
    """Returns the prime factors of a natural number."""
    if n < 0:
        return 0

    factors = []
    d = 2

    if n % d == 0:
        factors.append(d)
        while n % d == 0:
            n /= d

    d += 1

    while n > 1:
        if n % d == 0:
            factors.append(d)
            while n % d == 0:
                n /= d
        d += 2

    return factors


consecutive = []
i = 4

while len(consecutive) < 4:
    f = prime_factors(i)
    if len(f) == 4:
        if not consecutive:
            consecutive.append(i)
        else:
            if consecutive[-1] == i-1:
                consecutive.append(i)
            else:
                consecutive = [i]
    i += 1
    print(i)

print(consecutive[0])
