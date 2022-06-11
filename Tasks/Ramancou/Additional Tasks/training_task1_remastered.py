from math import prod
from itertools import pairwise, chain
variable = ['five thirteen two eleven seventeen two one thirteen ten four eight five nineteen',
            {'seventeen': 17, 'eight': 8, 'two': 2, 'one': 1, 'four': 4, 'thirteen': 13, 'five': 5, 'eleven': 11, 'nineteen': 19, 'ten': 10}]
for _ in variable[0].split(): variable[0] = variable[0].replace(_, str(variable[1][_]))
variable = list(pairwise(set(map(int, variable[0].split()))))
print(*list(map(lambda x: prod(x) if variable.index(x) % 2 == 0 else sum(x), variable)))
print(sum(filter(lambda x: x % 2 != 0, list(set(chain.from_iterable(variable))))))
