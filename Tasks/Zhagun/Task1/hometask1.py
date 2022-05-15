import decimal
initial_amount = decimal.Decimal('20000')
percent = decimal.Decimal('15')
years_amount = decimal.Decimal('5')
month_amount = years_amount * 12
final_amount = (initial_amount*(1+percent/100/12)**month_amount)
print ("the final amount will be", round(final_amount,2), "BYN" )