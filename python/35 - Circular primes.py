lim = 1000000
odd = [2]
sign = []
circular = 0
total = []
common = []

i = 1

while 1:
    num = 2*i + 1
    if num >= lim:
        break
    else:
        odd.append(num)
        i += 1

for x in range(0, len(odd)):
    sign.append(0)

num_dict = dict(zip(odd, sign))

end = int(lim**0.5)
p = 0
i = 1

while p < end:
    p = odd[i]
    multi = p**2

    while multi < lim:
        num_dict[multi] = 1
        multi += (2*p)

    i += 1

primes = [str(x) for x, y in num_dict.items() if y == 0]
s = set(primes)

for x in primes:
    combos = []
    end = len(x)
    for y in range(0, end):
        new = []
        for z in range(y, end + y):
            if z >= end:
                new.append(x[z-end])
            else:
                new.append(x[z])
        new = "".join(new)
        if new not in combos:
            combos.append(new)
    total += [combos]

for x in total:
    if set(x) <= s:
        common += x

common = list(set(common))
print(len(common))
