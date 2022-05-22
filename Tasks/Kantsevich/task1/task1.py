
import decimal

annual_interest_rate_prc = decimal.Decimal('15')
initial_capital_byn = decimal.Decimal('20000')
deposit_term_year = decimal.Decimal('5')
deposit_with_interest_byn = (initial_capital_byn * (1 + annual_interest_rate_prc/(100*12))**(deposit_term_year * 12))
print('Deposit with interest,BYN =', round(deposit_with_interest_byn,2))
