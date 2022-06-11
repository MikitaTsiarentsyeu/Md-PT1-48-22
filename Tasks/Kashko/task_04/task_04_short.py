from itertools import pairwise

numbers = 'five thirteen two eleven seventeen two one \
thirteen ten four eight five nineteen'

help_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20
}

# Transform into integers
numbers = [help_dict[n] for n in numbers.split()]
print(numbers)

# Delete duplicates and sort
numbers = list(set(numbers))
print(numbers)

# Calculate products of 1st and 2nd elements, sums of 2nd and 3rd, etc.
products_sums = [
    pair[0] * pair[1] if i % 2 == 0 else pair[0] + pair[1]
    for i, pair in enumerate(pairwise(numbers))
]
print(products_sums)

# Calculate sum of all odd numbers
odds_sum = sum([n for n in numbers if n % 2 != 0])
print(odds_sum)
