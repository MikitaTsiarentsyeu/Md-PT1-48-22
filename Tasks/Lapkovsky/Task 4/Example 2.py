# 2. Реализовать функцию is_prime которая получает на вход любое число больше нуля и выдаёт True, если число является простым, и False, если нет.
# is_prime(787) -> True
# is_prime(777) -> False

while True:
    
    number = int(input('Please, enter number > 0:\n'))
    try:
        if number <= 0:
            continue
        else:
            break
    except:
        break

def is_prime(number):
    if number == 1:
        return('Not prime!')
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