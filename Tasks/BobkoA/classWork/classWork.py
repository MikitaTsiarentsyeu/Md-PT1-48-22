
a= ["five thirteen two eleven seventeen two one thirteen ten four eight five nineteen", 
        {"one": 1, "two": 2, "three": 3, "four": 4, "five":5, "six": 6, "seven": 7, 
         "eight":8, "nine":9,"ten": 10, "eleven":11, "thirteen": 13, "fourteen": 14, "fifteen": 15, 
         16: "sixteen", "seventeen":17, "nineteen": 19, "twenty": 20,}]

a = sorted(set([a[1][i] for i in a[0].split()]))

print([a[1::2][i] + a[2::2][i] for i in range(min(len(a[1::2]), len(a[2::2])))])

print([a[::2][i]*a[1::2][i] for i in range(min(len(a[::2]), len(a[1::2])))])

print("сумма нечетных чисел = ", sum(i for i in a if i%2 !=0))

