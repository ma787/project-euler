fib_numbers = [1, 2]
length = 1

while length < 1000:
    final = str(fib_numbers[-1])
    new = fib_numbers[-1] + fib_numbers[-2]
    fib_numbers.append(new)
    length = len(final)

print(len(fib_numbers))