x = float(input('Please enter your investment, BYN:\n'))
y = float(input('Enter deposit term, years:\n'))
z = 15
S = x * (1+ z / 100) ** y
print('Total amount including 15 annual rule:', f"{S:,.2f} BYN")