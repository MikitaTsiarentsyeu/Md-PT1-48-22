data = ["five thirteen two eleven seventeen two one thirteen ten four eight five nineteen", {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,
                'six':6,'seven':7,'eight':8,'nine':9,'ten':10,
                'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,
                'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19}]


print('1. transform text to number\n')

data = [data[1][i] for i in data[0].split()]
print(data)

print('\n2. 3. delete dublicate and sort list\n')

data = list(set(data))
print(data)

print('\n4. multiply 1 and 2 value, sum 2 and 3 value ...\n')

data = list([data, 0])

for data[1] in range(len(data[0])):
    if data[1] + 1 == len(data[0]):
        data = list(data[0])
        break
    if data[1] % 2 != 0:
        print(f'{data[0][data[1]]} + {data[0][data[1] + 1]} = {data[0][data[1]] + data[0][data[1] + 1]}')
    if data[1] % 2 == 0:
        print(f'{data[0][data[1]]} * {data[0][data[1] + 1]} = {data[0][data[1]] * data[0][data[1] + 1]}')

print('\n5. sum odd elements\n')

print(sum(data for data in data if data % 2 != 0))

