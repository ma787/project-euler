num_letter = {
    1: 3,
    2: 3,
    3: 5,
    4: 4,
    5: 4,
    6: 3,
    7: 5,
    8: 5,
    9: 4,
    10: 3,
    11: 6,
    12: 6,
    13: 8,
    14: 8,
    15: 7,
    16: 7,
    17: 9,
    18: 8,
    19: 8,
    20: 6,
    30: 6,
    40: 5,
    50: 5,
    60: 5,
    70: 7,
    80: 6,
    90: 6,
    "hundred": 7,
    "thousand": 8
}

one_to_twenty = sum([num_letter[x] for x in range(1, 20)])

n = 20
double_digit = []

while n < 100:
    double_digit.append(num_letter[n])

    for x in range(1, 10):
        num = num_letter[n] + num_letter[x]
        double_digit.append(num)

    n += 10

dd_count = sum(double_digit)

hundreds = []
i = 1

for i in range(1, 10):
    third_digit = num_letter[i] + num_letter["hundred"]
    hundreds.append(third_digit)

    for x in range(1, 20):
        num = third_digit + 3 + num_letter[x]
        hundreds.append(num)

    for x in double_digit:
        num = third_digit + 3 + x
        hundreds.append(num)

thousand = num_letter[1] + num_letter["thousand"]
num_letter_count = one_to_twenty + dd_count + sum(hundreds) + thousand

print(num_letter_count)
