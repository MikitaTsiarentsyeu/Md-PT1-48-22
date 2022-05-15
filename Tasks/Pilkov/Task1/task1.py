budget = 20_000
years = 5
perсent = 15

def get_deposit_moneyback(start_budget, months_on_deposit, perсent):
    perсent = perсent/100
    return start_budget * (1 + perсent/12)**months_on_deposit

money_on_deposit_end = round(get_deposit_moneyback(budget, years*12, perсent), 2)

print(f"You will have {money_on_deposit_end} on your deposit after {years} years")
