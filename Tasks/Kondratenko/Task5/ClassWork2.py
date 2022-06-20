lst = ['1', '11', '12', '22', '2', '13', '30', '33']

print(list(map(str, sorted(filter(lambda x: x % 2, map(int, lst))))))