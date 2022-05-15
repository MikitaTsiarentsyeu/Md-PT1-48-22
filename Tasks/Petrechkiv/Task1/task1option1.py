import decimal
initial_amount = decimal.Decimal(20000)
percent = decimal.Decimal(15)
number_of_years = decimal.Decimal(5)
number_of_months = number_of_years * 12
final_amount = (initial_amount*(1+percent/100/12)**number_of_months)
print ("the amount on the account at the end of the specified period", round(final_amount,2)) 