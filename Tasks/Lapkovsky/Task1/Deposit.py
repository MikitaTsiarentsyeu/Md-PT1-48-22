# Task condition

С = 20000
r = 15
y = 5
m = 12

# Calculating income with monthly capitalization

S = (С*(1+r/100/m)**(m*y))
print("Deposit amount at the end of the term = ", round((S),2), "BYN")


# Another solution

def bank (a, years):

    for i in range (years):

        a = (С*(1+r/100/m)**(m*y))

    return (a)

result = bank (float(input("Введите сумму вклада: ")), int(input("На сколько лет: ")))

print (round((result),2), "BYN")
