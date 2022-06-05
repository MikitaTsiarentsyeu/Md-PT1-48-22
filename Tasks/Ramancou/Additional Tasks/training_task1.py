variable = ['five thirteen two eleven seventeen two one thirteen ten four eight five nineteen',
            {'seventeen': 17, 'eight': 8, 'two': 2, 'one': 1, 'four': 4, 'thirteen': 13, 'five': 5, 'eleven': 11, 'nineteen': 19, 'ten': 10}]
for _ in variable[0].split(): variable[0] = variable[0].replace(_, str(variable[1][_]))
variable = list(set(map(int, variable[0].split())))
print(*list(map(lambda x: variable[x] * variable[x + 1] if x % 2 == 0 else variable[x] + variable[x + 1], range(9)))) # Calculate products of 1 and 2elements, sums of 2 and 3, etc.
print(sum([i for i in variable if i % 2 != 0]))  # Calculate sum of odd numbers
