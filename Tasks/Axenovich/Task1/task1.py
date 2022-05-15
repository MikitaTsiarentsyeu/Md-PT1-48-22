from decimal import *
print('Calculating a deposit with monthly capitalisation\n')

deposit = Decimal(input('Input your deposit amount(BYN): '))
percent = Decimal(input('Input annual deposit interest(%): '))
years = Decimal(input('Input term of the deposit(years): '))

result = round(deposit * ((1 + percent/100/12)**(years*12)), 2)

print(f"Your {deposit} BYN after {years} {'years' if years > 1 else 'year'} with {percent}% per year will be {result} BYN")