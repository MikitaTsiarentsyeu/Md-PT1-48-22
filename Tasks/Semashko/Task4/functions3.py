#origin = [0, 1, 2, 3, 4, 7, 8, 10]
#origin = [4, 7, 10]
origin = [2, 3, 8, 9]

def get_range(origin):
    result_list = []
    temp_list = []
    for index, val in enumerate(origin):
        temp_list.append(val)

        if not ((index < len(origin)-1) and (origin[index] + 1 == origin[index+1])):

            if len(temp_list) > 1:
                result_list.append(f'{temp_list[0]} - {temp_list[-1]}')
            else:
                result_list.append(f'{temp_list[0]}')

            temp_list.clear()

    return' , '.join(result_list)

print(get_range(origin))


# Not my variant, just copied it for myself.

#l = [0, 1, 2, 3, 4, 7, 8, 10]
#l = [4, 7, 10]
# l = [2, 3, 8, 9]

# def get_ranges(l):
#     list = f'{l[0]}'
#     Flag = False
#     for i in range(len(l) - 1):
#         if l[i + 1] - l[i] == 1:
#             Flag = True
#         else:
#             if Flag:
#                 list += f'-{l[i]}, {l[i + 1]}'
#             else:
#                 list += f', {l[i + 1]}'
#             Flag = False
#     if Flag:
#         list += f'-{l[-1]}'
#     return print(list)

# get_ranges(l)
