def maker(n):
    def inner(x):
        return x**n
    return inner

square = maker(2)
print(square(2), square(3), square(4))

cube = maker(3)
forth = maker(4)

l = [maker(i) for i in range(1, 101)]
print([func(2) for func in l])