import timer

timer.start()
for i in range(100000000):
    i**2

print(timer.finish())