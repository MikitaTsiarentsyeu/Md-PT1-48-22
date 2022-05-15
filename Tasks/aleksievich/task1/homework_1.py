d = int(input("Enter the deposit amount, BYN\n"))
n = int(input("Enter bank interest rate, %\n"))
t = int(input("Enter period of deposit, years\n"))
print(" 1 daily capitalization\n 2 monthly capitalization\n 3 quarterly capitalization")
print(" 4 semi-annual capitalization\n 5 annual capitalization")
period = int(input("Choose one of the capitalization periods: 1, 2, 3, 4 or 5\n"))
if period == 1:
    p = 365
elif period == 2:
    p = 12
elif period == 3:
    p = 4
elif period == 4:
    p = 2
elif period == 5:
    p = 1
else:
    print("You have a one-time capitalization.")
    p = 1/t
s = round(d * (1 + n/100/p) ** (t * p))
print("At the end of the period total amount on your account will be", s, "BYN")