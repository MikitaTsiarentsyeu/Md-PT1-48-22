x = 20000
# x - Initial amount
a = 15
# a - precent
b = 5
# b - deposit term
c = 12
# C - number of months in a year
d = x * ((1 + ((a/100)/c))**(b*c))
# d - Final amount
print ("Your final amount",(d))