
 

def check_str(text:str):
    return (sum(map(str.isupper, text))),(sum(map(str.islower, text)))
print(check_str("The quick Brown Fox"))


def is_prime(number):
    for j in range(2,number):
        if (number%j == 0):
            return False
    return True        
print(is_prime(787))
print(is_prime(777))        


def get_ranges(numbers):
    numbers = sorted(set(numbers))
    range_start = previous_number = numbers[0]
    for number in numbers[1:]:
        if number == previous_number + 1:
            previous_number = number
        else:
            yield f'{range_start} - {previous_number}'
            range_start = previous_number = number
    yield f'{range_start} - {previous_number}'       
print(list(get_ranges([0, 1, 2, 3, 4, 7, 8, 10])))
print(list(get_ranges([4,7,10])))
print(list(get_ranges([2, 3, 8, 9]))) 


   
    
 


