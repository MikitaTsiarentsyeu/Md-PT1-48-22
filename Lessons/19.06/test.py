l = ['1', '11', '12', '22', '2', '13', '30', '33'] 

print(sorted(filter(lambda x: int(x) % 2 == 0, l), key=int))