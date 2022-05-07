p = int(input("Please enter the amount of your deposit (BYN):\n"))
y = int(input("Term of deposit (years):\n"))
per = float(input("Fixed annual interest rate (%):\n"))

S = p * ((1 + (per / 100 / 12)) ** (12 * y))

print(round(S, 2))

