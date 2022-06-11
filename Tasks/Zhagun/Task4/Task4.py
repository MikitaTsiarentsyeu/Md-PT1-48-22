
dict= ['five thirteen two eleven seventeen two one thirteen ten four eight five nineteen', {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,
'eight':8,'nine':9,'ten':10,'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fiveteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19,'twenty':20}]
dict=list(set([dict[1][i] for i in dict[0].split()]))
print(dict)
for i in range(min(len(dict[1::2]), len(dict[2::2]))):
    print('sum:', dict[1::2][i] + dict[2::2][i]) 
for i in range(min(len(dict[::2]), len(dict[1::2]))):
        print('multiplication:', dict[::2][i]*dict[1::2][i])
print('sum of odd numbers is', sum(i for i in dict if i%2 !=0))