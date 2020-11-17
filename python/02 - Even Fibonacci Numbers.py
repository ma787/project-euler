sequence = [1,2]
num_list = [2]

while sequence[-1] < 4000000:
    sequence.append(sequence[-1] + sequence[-2])
    if sequence[-1]%2 == 0 and sequence[-1] < 4000000:
        num_list.append(sequence[-1])

print(sum(num_list))
