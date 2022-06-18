
while True:
    number = int(input('Enter any number bigger than 0:\n'))
    try:
        if number <= 0:
            continue
        else:
            break
    except:
        break

# First variant

def is_prime(number):
    if number == 2 or number == 3:
        return True
    if number % 2 == 0:
        return False
    if number == 1:
        return ('Not prime nor complex')
    for i in range(3, int(number**0.5)+1, 2):
        if number % i == 0:
            return False
    return True

print(is_prime(number))

# Second variant

def is_prime(number):
    if number == 1:
        return('Not prime nor complex')
    counter = 0
    for i in range(1, number+1):
        if number % i == 0:
            counter += 1
        else:
            continue
    if counter > 2:
        return False
    else:
        return True

print(is_prime(number))