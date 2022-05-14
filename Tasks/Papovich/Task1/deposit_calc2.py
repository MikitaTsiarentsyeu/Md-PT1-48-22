import decimal
d = int(input('enter deposit: BYN\n')) 
p = int(input('enter perecent: %\n')) 
t = int(input('enter number of months: m\n'))
s = decimal.Decimal(d*(1+p/(100*12))**t)
print('Total payout amount', ("%.2f" % s), 'BYN')