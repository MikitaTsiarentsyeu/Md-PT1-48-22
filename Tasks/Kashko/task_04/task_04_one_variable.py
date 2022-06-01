from functools import partial
from itertools import compress, zip_longest

# Transform into integers, delete duplicates and sort
numbers = list(
    set(
        map({
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
        }.get, 'five thirteen two eleven seventeen two one \
thirteen ten four eight five nineteen'.split())))
print(numbers)

# Calculate products of 1st and 2nd elements, sums of 2nd and 3rd, etc.
print(
    list(
        filter(
            None,
            sum(
                zip_longest(map(int.__mul__, numbers[::2], numbers[1::2]),
                            map(int.__add__, numbers[1::2], numbers[2::2])),
                ()))))

# Calculate sum of all odd numbers
print(sum(compress(numbers, map(partial(int.__rmod__, 2), numbers))))
