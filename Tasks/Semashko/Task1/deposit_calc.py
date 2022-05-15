import decimal

P = decimal.Decimal(input('Enter your deposit (BYN):\n'))
N = decimal.Decimal(input('Enter annual percent (%):\n'))
Y = int(input('How many years?\n'))

S = P * (1 + N / 100 / 12) ** (Y * 12)

# format S 2 signs after "."
print ('Total sum: {:.2f} BYN'.format(S))