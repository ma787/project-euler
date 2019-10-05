with open("p067_triangle.txt", "r") as f:
    pyramid = f.read()

rows = pyramid.split("\n")
rows = [x.split() for x in rows]

for x in rows:
    for i in x:
        j = x.index(i)
        x[j] = int(i)

lim = len(rows) - 2

for num in range(lim, -1, -1):
    current = rows[num]
    below = rows[num + 1]

    for pos, elem in enumerate(current):
        opt1 = below[pos]
        opt2 = below[pos + 1]

        path = elem + max((opt1, opt2))
        current[pos] = path

print(rows[0][0])
