#1.Реализовать функцию check_str которая получает на вход непустую строку и выдаёт информацию о количестве букв в верхнем и нижнем регистре.
#check_str('The quick Brown Fox') -> '3 upper case, 12 lower case'

text_line = ('The quick Brown Fox')

def check_str(text_line):
    counter_of_upper = 0
    counter_of_lower = 0
    for i in text_line:
        if i.isupper():
            counter_of_upper +=1
        if i.islower():
            counter_of_lower +=1
    text_line_with_info = f"Counter of upper register is {counter_of_upper}, counter of lower register is {counter_of_lower}"
    return text_line_with_info                   
print(check_str(text_line))


#2. Реализовать функцию is_prime которая получает на вход любое число больше нуля и выдаёт True, если число является простым, и False, если нет.
#is_prime(787) -> True
#is_prime(777) -> False

def is_prime(n):
    for i in range(2,n):
        if n%i ==0:
            return False
    return True
         
n = int(input())         
print(is_prime(n))

#3. Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел, 
#отсортированных по возрастанию, и которая этот список “сворачивает”.

#get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
#get_ranges([4,7,10])  -> "4, 7, 10"
#get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"

list_for_exp = [0, 1, 2, 3, 4, 7, 8, 10]
def get_ranges(list_for_exp):
    list_of_ranges = []
    current_range = []
    for i,e in enumerate(list_for_exp):
        current_range.append(e)
        if not (i <len(list_for_exp)-1 and list_for_exp[i+1] - e ==1):
            if len(current_range)==1:
                list_of_ranges.append(str(current_range[0]))
            else:
                list_of_ranges.append(str(current_range[0])+ ' - ' + str(current_range[-1])) 
            current_range.clear()
    return ','.join(list_of_ranges)

print(get_ranges(list_for_exp))
        
