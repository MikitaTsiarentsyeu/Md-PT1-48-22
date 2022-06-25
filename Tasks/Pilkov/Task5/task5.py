def sum_all_inner_elements(num_list : list) -> object:
    sum = 0
    for v in num_list:
        if type(v) is list:
            sum += sum_all_inner_elements(v)
        else:
            sum += v
    return sum

print(sum_all_inner_elements([1, 2, [2, 4, [[7, 8], 4, 6]]]), ' -> ', 34)


def fib(num : int) -> list:
    if num < 1:
        return None
    elif num == 1:
        return [0, ]
    elif num == 2:
        return [0, 1]
    else:
        tmp_list = fib(num - 1)
        tmp_list.append(tmp_list[-2] + tmp_list[-1])
        return tmp_list

print(fib(5),' -> ', [0,1,1,2,3])
print(fib(10),' -> ', [0,1,1,2,3,5,8,13,21,34])