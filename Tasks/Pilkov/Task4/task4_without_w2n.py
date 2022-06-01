program_dict = {
    'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
    'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixtheen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20,
    'data': "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"
}

program_dict['data'] = program_dict['data'].split()

program_dict['data'] = [program_dict[value] for _, value in enumerate(program_dict['data'])]

program_dict['data'] = list(set(program_dict['data']))

for key in range(0, len(program_dict['data']) - 1):
    if key % 2 == 1:
        print(f'Sum of {key} and {key+1}: ', program_dict['data'][key] + program_dict['data'][key+1])
    else:
        print(f'Product of {key} and {key + 1}: ', program_dict['data'][key] * program_dict['data'][key+1]) 

print('Sum of all values', sum([value for value in program_dict['data'] if value%2]))