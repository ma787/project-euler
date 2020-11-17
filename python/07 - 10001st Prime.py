pf_list = [2]
n = 3

while len(pf_list) < 10001:
    m = int(n**0.5)
    factors = [x for x in range(2,m+1) if n%x == 0]
    if not factors:
        pf_list.append(n)
    n += 2

print(pf_list[-1])
