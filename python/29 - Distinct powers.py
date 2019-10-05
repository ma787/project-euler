powers = []

for a in range(2, 101):
    for b in range(2, 101):
        num = a**b
        powers.append(num)

powers = list(set(powers))
powers = sorted(powers)
print(len(powers))