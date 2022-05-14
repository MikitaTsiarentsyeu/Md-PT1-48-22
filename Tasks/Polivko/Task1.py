

start_sum = int(input("Enter dep (BYN): "))
period = int(input("Enter period (years): "))
persent = int(input("Enter persent (yearlong): "))/100
result = start_sum * (1 + (persent / 12)) ** (period * 12)
print(f'Your depozit after {period} years {round(result, 2)} BYN')