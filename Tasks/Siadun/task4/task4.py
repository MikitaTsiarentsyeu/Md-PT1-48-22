from word2number import w2n
two_var=[]
one_var = set(("five thirteen two eleven seventeen two one thirteen ten four eight five nineteen").split())
for n in one_var:
    two_var.append(w2n.word_to_num(n))
f = sorted(two_var)
print(f)
for n in range(len(f)):
    if n % 2 == 0:
        x = f[n]*f[n+1]
        print("product of numbers: ", x)
    elif n ==  len(f) - 1:
        break
    else:
        a = f[n]+f[n+1]
        print("sum of numbers: ", a)
i = 0
for n in f:
    if n % 2 ==1:
        i += n
    else:
        pass
print("sum of odd numbers: ", i)