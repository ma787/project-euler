def recurring(num, div):
    decimals = []
    remainders = []

    while 1:
        while num < div:
            num *= 10

        if num in remainders:
            return decimals

        remainders.append(num)

        quotient = num // div
        remainder = num % div

        decimals.append(quotient)

        if remainder == 0:
            return [0]

        else:
            num = remainder

lengths = []

for x in range(1, 1001):
    repetend = recurring(1, x)
    lengths.append(len(repetend))

max_length = max(lengths)
print(lengths.index(max_length) + 1)
