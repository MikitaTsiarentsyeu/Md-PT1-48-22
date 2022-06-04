numbers = ['five thirteen two eleven seventeen two one thirteen ten four eight five nineteen',
           {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11,
            'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19,
             'twenty': 20}]
numbers = list({numbers[1][n] for n in numbers[0].split()})
print(f'numbers: {numbers}\n'
      f'The product of numbers: {[numbers[::2][n] * numbers[1::2][n] for n in range(min(len(numbers[::2]), len(numbers[1::2])))]}\n'
      f'Sum of numbers: {[numbers[1::2][n] + numbers[2::2][n] for n in range(min(len(numbers[1::2]), len(numbers[2::2])))]}\n'
      f'The sum of odd numbers: {sum([n for n in numbers if n % 2 != 0])}')
