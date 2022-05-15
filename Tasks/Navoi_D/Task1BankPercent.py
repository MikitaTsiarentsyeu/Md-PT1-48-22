from decimal import *

print("calculation of interest for deposit")

Deposit = int(input("input deposit amount ="))
TenureInYears = int(input("input deposit tenure in years ="))
Rate = int(input("input deposit interest rate ="))

TenureInMonth = TenureInYears*12

# Calculating total amount for every month capitalization of interest

TotalAmount = Decimal(Deposit*(1 + (Rate/12)/100)**TenureInMonth)

# rounding up two digits after the decimal point

rounded = TotalAmount.quantize(Decimal('0.01'), rounding = ROUND_HALF_UP)

print("Your total amount is:", rounded)

