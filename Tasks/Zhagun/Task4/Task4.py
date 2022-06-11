def check_str(string):
    counter={'upper_case':0,'lower_case':0}
    for i in string:
        if i.isupper():
            counter['upper_case']+=1
        elif i.islower():
            counter['lower_case']+=1
        else:
            pass
    print('initial string - ',string,)
    print(counter['upper_case'],'upper case,',counter['lower_case'],'lower case')
check_str('My name is Veronika Zhagun')

def isPrime(num):
    return all(num % i for i in range(2,int(num**0.5)-1))
print ('Number 787 is ', isPrime(787))
print ('Number 777 is ', isPrime(777))

def get_ranges(l):
    list = f'{l[0]}'
    Flag = False
    for i in range(len(l) - 1):
        if l[i + 1] - l[i] == 1:
            Flag = True
        else:
            if Flag:
                list += f'-{l[i]}, {l[i + 1]}'
            else:
                list += f', {l[i + 1]}'
            Flag = False
    if Flag:
        list += f'-{l[-1]}'
    return print(list)
get_ranges([0,1,2,4,7,8,9,16])


