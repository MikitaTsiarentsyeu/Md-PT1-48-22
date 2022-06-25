def list_sum(rec_list):
    if isinstance(rec_list, (list,set,tuple)):
        final_sum = 0
        for item in rec_list:
            final_sum = final_sum + list_sum(item)
        return final_sum
    else:
        return rec_list
test_list = [1, [2, 3], [0], [[2, 3, 4], 2], 1, 0, [[[3]]]]
print(list_sum(test_list))                