numbers = []
x = 1
step = 2
count = 0

while x <= 1002001:
    numbers.append(x)
    if count == 4:
        count = 0
        step += 2
    x += step
    count += 1

print(sum(numbers))