import re


def calc_deposit_balance(start_deposit: float, years: int,
                         annual_rate: float) -> str:

    income = start_deposit * (1 + annual_rate / (100 * 12))**(years*12)
    income = income
    profit = income - start_deposit
    result = f'Your income: {round(income, 2)} BYN. '\
             f'Your profit: {round(profit, 2)} BYN'
    return result


def get_user_input() -> tuple:

    r = re.compile(r'^\d{0,}\.{,1}(?!$)\d{,2}$')

    while True:
        sum_ = str.strip(input('Enter start deposit, BYN (e.g. 20000.00)\n'))
        if re.match(r, sum_) is None:
            print('Invalid data! Try once more, please!')
            continue
        sum_ = round(float(sum_), 2)
        break

    while True:
        term = str.strip(input('Enter deposit terms, years (e.g. 5)\n'))
        if re.match(r, term) is None:
            print('Invalid data! Try once more, please!')
            continue
        if term.find('.') != -1:
            term = int(term[:term.index('.')])
        else:
            term = int(term)
        break

    while True:
        rate = str.strip(input('Enter an annual rate, % (e.g. 15.00)\n'))
        if re.match(r, rate) is None:
            print('Invalid data! Try once more, please!')
            continue
        rate = round(float(rate), 2)
        break

    return (sum_, term, rate)


data = get_user_input()
income = calc_deposit_balance(*data)
print(income)
