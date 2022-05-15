import math

a = 20000
persent = 0.15
term = 5
s = a * ((1 + persent / 12) ** (term * 12))
print( "account amount = %.3f" % s)
