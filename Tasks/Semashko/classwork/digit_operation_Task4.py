# all numbers more than 0 and less than 21

string = 'five thirteen two eleven seventeen two one ten four eight five nineteen'

numbers = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
            'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
            'eighteen': 18, 'nineteen': 19, 'twenty': 20}

# converting into numbers iteration by dictionary
digit = [v for k,v in numbers.items() if k in string.split()]
print(digit)

# converting into numbers iteration by string
# digit = []
# for l in string.split():
#     digit.append(numbers[l])
# print(list(set(digit)))

# display sums and multiplies

print(f'Multiply list: {[digit[k] * digit[k+1] for k in range(len(digit)-1) if k % 2 == 0]}')
print(f'Sum list: {[digit[k] + digit[k+1] for k in range(len(digit)-1) if k % 2 != 0]}')
# for k in range(len(digit)-1):
#     if k % 2 == 0:
#         #print(k)
#         print(f'Multiply:{digit[k] * digit[k+1]}')
#     else:
#         #print(k)
#         print(f'Sum:{digit[k] + digit[k+1]}')

# display sum of all odds

print(f'Sum of odds: {sum([i for i in digit if i % 2 != 0])}')
# summa = 0
# for i in digit:
#     if i % 2 != 0:
#         summa += i
# print(f'Sum odds: {summa}')
