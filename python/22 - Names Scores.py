import string
from functools import reduce


with open("p022_names.txt", "r") as f:
    names = f.read()

names = names.replace("\"", "")
names = names.split(",")
names = sorted(names)

numbers = [x for x in range(1, 27)]
alphabet = list(string.ascii_lowercase)
letter_to_num = dict(zip(alphabet, numbers))

name_scores = []

for i, name in enumerate(names, start=1):
    name = name.lower()
    name_score = []
    for letter in name:
        name_score.append(letter_to_num[letter])
    name_score = reduce(lambda x, y: x+y, name_score)
    name_score *= i
    name_scores.append(name_score)

total = sum(name_scores)
print(total)