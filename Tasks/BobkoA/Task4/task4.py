import math

#task 1
def check_str(s):
 count_lower = 0
 count_upper = 0
 i = 0
 while i < len(s):
  if s[i].islower(): count_lower += 1
  if s[i].isupper(): count_upper += 1
  i += 1
 print(count_upper, "upper case,", count_lower, "lower case")

check_str("The quick Brown Fox")

#task 2

def is_prime(arg):
    for i in range(2, int(math.sqrt(arg)) + 1):
        if arg % i == 0:
            return False
    return True
print(is_prime(787))
print(is_prime(777))

# task 3
def get_ranges(my_list):
    i = 0
    while i < len(my_list):
        start = i
        while i < len(my_list)-1 and my_list[i] >= my_list[i+1]-1:
            i += 1
        print(my_list[start] if my_list[start] == my_list[i] else "%d-%d" % (my_list[start], my_list[i]),
              end="," if i < len(my_list)-1 else "\n")
        i += 1

get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  
get_ranges([4,7,10])  
get_ranges([2, 3, 8, 9])