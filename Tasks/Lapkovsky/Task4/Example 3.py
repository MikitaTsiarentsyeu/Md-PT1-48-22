#3. Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел, 
# отсортированных по возрастанию, и которая этот список “сворачивает”.

# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
# get_ranges([4,7,10])  -> "4, 7, 10"
# get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"

#l = [0, 1, 2, 3, 4, 7, 8, 10]
#l = [4, 7, 10]
l = [2, 3, 8, 9]

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
get_ranges(l)