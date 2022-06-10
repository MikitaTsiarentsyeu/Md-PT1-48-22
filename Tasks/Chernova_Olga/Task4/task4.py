def check_str(text: str) -> str: 
    """This function counts the number of lowercase 
    and uppercase letters in a string\n
    text - any string"""
    text = ''.join(text.split())
    counter = 0
    for i in text:
        if i.islower():
            counter += 1
    print(f'There are {len(text) - counter} upper case and {counter} lower case')

check_str('ThiS is TEST texT for ThE tasK')



def is_prime(num: int) -> bool:
    """This function determines whether the number is prime or not\n
    num - positive integer greater than 0""" 
    if num == 2:
        print('True')
    elif num == 1 or num % 2 == 0:
        print('False')
    else:
        work_num = 3
        while work_num ** 2 <= num:
            if num % work_num == 0:
                print('False')
            work_num += 2
        print('True')
                    
is_prime(149)



def get_ranges(l:list) -> str: 
    """This function collapses the list. If the numbers are in order, then 
    the first and final numbers are hyphenated. If the number is one, then this number 
    is output.
    l - a list with non-repeating integers sorted in ascending order"""
    list_of_output = []
    counter = 0
    while counter < len(l):
        work_list = []
        work_list.append(str(l[counter]))
        if str(l[-1]) not in work_list:
            for i in range(counter,len(l)-1):
                if l[i] +1 == l[i+1]:
                    work_list.append(str(l[i+1]))
                else:
                    break
            if len(work_list) > 1:
                list_of_output.append(f'{work_list[0]}-{work_list[-1]}')
            else:
                list_of_output.append(work_list[0])
            counter = i+1
            if str(l[-1]) in work_list:
                break
        else:
            list_of_output.append(work_list[0])
            break
    print(', '.join(list_of_output))
        
            
get_ranges([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20])