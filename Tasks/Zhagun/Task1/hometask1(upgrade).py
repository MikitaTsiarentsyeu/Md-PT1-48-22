import decimal
initial_amount = decimal.Decimal(input('Enter initial deposit ',))
percent = decimal.Decimal(input('Enter annual percentage ',))
years_amount = decimal.Decimal(input('Enter number of years ',))
month_amount = years_amount * 12
final_amount = (initial_amount*(1+percent/100/12)**month_amount)
print ("the final amount will be", round(final_amount,2), "BYN" )