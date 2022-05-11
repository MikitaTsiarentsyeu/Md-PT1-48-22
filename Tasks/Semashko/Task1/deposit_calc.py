# How can we use Decimal to get the tolerance we want???
P = float(input('Enter your deposit (BYN):\n'))
N = float(input('Enter annual percent (%):\n'))
Y = int(input('How many years?\n'))

S = P * (1 + N / 100 / 12) ** (Y * 12)
# format S 3 signs after "."
print ('Total sum: {:.2f} BYN'.format(S))