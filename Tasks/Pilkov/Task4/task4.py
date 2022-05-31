from word2number import w2n

data = "five thirteen two eleven seventeen two \
one thirteen ten four eight five nineteen"

data = data.split()

data = [w2n.word_to_num(value) for _, value in enumerate(data)]

data = list(set(data))

[print(f'Sum of {key} and {key+1}: ', data[key] + data[key+1]) if key % 2 == 1 else print(f'Product of {key} and {key + 1}: ', data[key] * data[key+1]) for key in range(0, len(data) - 1)]

print('Sum of all values', sum([value for value in data if value%2]))