eq = input("Please enter the eq:\n")
x = int(input("Please enter the x value:\n"))

eq = eq.replace(' ', '').replace('y=', '')
print(eq, x)
parts = eq.split('x')
k = int(parts[0])
b = int(parts[1])

y = k*x + b
print(y)
