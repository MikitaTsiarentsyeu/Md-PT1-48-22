def check_str(s):
    if s and not s.isspace():
        up = 0
        low = 0
        for i in s: 
            if i.isupper():
                up +=1
            elif i.islower():
                low +=1 
        return f"{up} upper case, {low} lower case"
    else:
        return "string is empty"
print(check_str("The quick Brown Fox")) 


def is_prime(n):
    k = 0
    for i in range(1, n + 1):
        if n % i == 0:
            k += 1
    if k == 2:
        return True
    else:
        return False
print(is_prime(787))
print(is_prime(777))


def get_ranges(N_list):
    N_list = [int(i) for  i in N_list]
    N_list = set(N_list)
    N_list = sorted(list(N_list))
    prev_number = N_list[0]
    pagelist = []

    for number in N_list:
        if number != prev_number + 1:
            pagelist.append([number])
        elif len(pagelist[-1]) > 1:
            pagelist[-1][-1] = number
        else:
            pagelist[-1].append(number)
        prev_number = number

    return ','.join(['-'.join(map(str,page)) for page in pagelist])

print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4,7,10]))
print(get_ranges([2, 3, 8, 9]))