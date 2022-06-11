def scheck_str(string): 
    lower_case = 0 
    upper_case = 0 
    for letter in string: 
        if letter.isupper(): 
            upper_case += 1 
        elif letter.islower(): 
            lower_case += 1
    print(f"{upper_case} upper case, {lower_case} lower case")
scheck_str("The quick Brown Fox")


def is_prime(number_to_chek):
    for x in range(2, number_to_chek):
        if (number_to_chek % x == 0):
            return False
    return True
print(is_prime(787))
print(is_prime(777))


def get_ranges(sorted_lst):
        i = 0
        collapsed_list = [[sorted_lst[0], sorted_lst[0]]]
        for j in sorted_lst:
            if collapsed_list[i][1] in (j, j-1):
                collapsed_list[i][1] = j
            else:
                collapsed_list.append([j, j])
                i += 1
        collapsed_list_str = ""
        for k in collapsed_list:
            if k[0] != k[1]:
                collapsed_list_str = f"{collapsed_list_str},{k[0]}-{k[1]}"
            else:
                collapsed_list_str = f"{collapsed_list_str},{k[0]}"
        return collapsed_list_str[1:]
print(f"\"{get_ranges([0, 1, 2, 3, 4, 7, 8, 10])}\"")
print(f"\"{get_ranges([4,7,10])}\"")
print(f"\"{get_ranges([2, 3, 8, 9])}\"")