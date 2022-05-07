annual_interest_rate_prc = 15
initial_capital_byn = 20000
deposit_term_year = 5
deposit_with_interest_byn = (initial_capital_byn * (1 + annual_interest_rate_prc/(100*12))**(deposit_term_year * 12))
print('Deposit with interest,BYN =', deposit_with_interest_byn)