Letters_into_numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
                        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
                        'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
                        'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20}

user_letters = input('Please, enter the numbers from 1 to 20 in words: ').split(' ')

user_numbers = {Letters_into_numbers[i] for i in user_letters}
sorted_user_numbers = sorted(user_numbers)
sum = 0
for i in range(len(sorted_user_numbers)):
    if i != len(sorted_user_numbers)-1:
        if i%2 == 0:
            print(sorted_user_numbers[i]*sorted_user_numbers[i+1])
        else:
            print(sorted_user_numbers[i] + sorted_user_numbers[i + 1])
    if sorted_user_numbers[i]%2 ==1:
       sum +=  sorted_user_numbers[i]

print("Sum of odd user numbers is ", sum)
