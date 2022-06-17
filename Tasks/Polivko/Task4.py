def check_str(string):
    lower = 0
    upper = 0
    for i in string:
        if i.islower():
            lower += 1
        else:
            upper += 1
    return f'{upper} upper case, {lower} lower case'


print(check_str('The quick Brown Fox'))


def is_prime(number):
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
        return True


print(is_prime(787))
print(is_prime(777))


def get_ranges(numbers):
    interval = []
    first = last = numbers[0]

    for n in numbers[1:] + [""]:
        if n != last + 1:
            if last == first:
                interval.append(f"{first}")
            elif last != first:
                interval.append(f"{first}-{last}")
            first = n
        last = n

    return ", ".join(interval)


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 8, 10]))
print(get_ranges([2, 3, 7, 8, 9]))


