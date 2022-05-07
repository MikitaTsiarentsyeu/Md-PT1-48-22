print('Calculating a deposit with monthly capitalisation\n')

deposit = int(input('Input your deposit amount(BYN): '))
percent = int(input('Input annual deposit interest(%): '))
years = int(input('Input term of the deposit(years): '))

result = deposit * ((1 + percent/100/12)**(years*12))

print(f'Your {deposit} BYN after {years}', 'years' if years > 1 else 'year', f'with {percent}% per year will be {int(result)} BYN')