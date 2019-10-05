coins = (1, 2, 5, 10, 20, 50, 100, 200)
states = [0 for x in range(1, 202)]
states[0] = 1

for x in coins:
    for num in range(x, 201):
        states[num] += states[num - x]

print(states[200])
