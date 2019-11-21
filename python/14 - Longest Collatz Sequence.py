n = 3
lengths = [4, 2]
collatz = {}

while n <= 1000000:
    seq = [n]
    a = n
    while a > 1:
        try:
            for x in collatz[a]:
                seq.append(x)
            break
        except KeyError:
            if a % 2 == 0:
                a /= 2
                seq.append(a)
            else:
                a = 3*a + 1
                seq.append(a)
                a /= 2
                seq.append(a)
    l = len(seq)
    collatz[n] = seq
    lengths.append(l)
    n += 1

maxl = max(lengths)
print(lengths.index(maxl)+1)
