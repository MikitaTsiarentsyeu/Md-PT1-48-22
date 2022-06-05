
numbers_v= ("five thirteen two eleven seventeen two one thirteen ten four eight five nineteen") 
dictionary_num = {"zero": 0 ,"one": 1,"two":2,"tree":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,
"nine":9,"ten":10,"eleven":11,"twelwe":12,"thirteen":13,"fourteen":14,"fifteen":15,"sixteen":16,
"seventeen":17,"eigthteen":18,"nineteen":19,"twenty":20,"twenty one":21}
l=[]
for i in numbers_v.split(" "):
        l.append(dictionary_num[i])         
        sorted(list(set(l)))
even_numder = []
odd_number = []
for n,v in enumerate(sorted(list(set(l)))):
        if n%2 == 0:
            even_numder.append(v)    
        else: 
            odd_number.append(v)    
print("Multiplication result:",([x * y for x, y in zip(even_numder, odd_number)]))
print("Addition result:",[x + y for x, y in zip(even_numder, odd_number[1::])])
print("Sum of odd numbers:",sum(i for i in sorted(list(set(l))) if i%2 !=0))

    



