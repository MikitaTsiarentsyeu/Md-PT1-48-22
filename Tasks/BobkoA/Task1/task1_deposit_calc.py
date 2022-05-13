
D = 20000
r = 15
y = 5
n = 12

# Option 1 (banking formula)

S = (D*(1+r/100/n)**(n*y))
print("Cумма депозита в конце срока (формула 1) = ", round((S),2), "BYN")

# Option 2

for i in range(n*y):
    D = D + D * (r/(n*100))
print("Сумма депозита в конце срока (формула 2) = ", round((D),2), "BYN")








