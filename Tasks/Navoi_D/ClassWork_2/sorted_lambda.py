l = ['1', '11', '12', '22', '2', '13', '30', '33']
print(list(map(str,(list(filter(lambda x: (x^2) % 2 == 0,sorted(list(map(int,l)))))))))
