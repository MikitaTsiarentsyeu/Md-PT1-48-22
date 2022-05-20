from datetime import datetime as dt
hour_dict = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь',
             9: 'девять', 10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'один', 14: 'два', 15: 'три',
             16: 'четыре', 17: 'пять', 18: 'шесть', 19: 'семь', 20: 'восемь', 21: 'девять', 22: 'десять',
             23: 'одиннадцать', 24: 'двенадцать'}
hour_dict2 = {1: 'первого', 2: 'второго', 3: 'третьего', 4: 'четвертого', 5: 'пятого', 6: 'шестого', 7: 'седьмого',
              8: 'восьмого', 9: 'девятого', 10: 'десятого', 11: 'одиннадцатого', 12: 'двенадцатого', 13: 'первого',
              14: 'второго', 15: 'третьего', 16: 'четвертого', 17: 'пятого', 18: 'шестого', 19: 'седьмого',
              20: 'восьмого', 21: 'девятого', 22: 'десятого', 23: 'одиннадцатого', 24: 'двенадцатого'}
min_dict = {1: 'одна', 2: 'две', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять',
            10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать',
            16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать', 20: 'двадцать', 30: 'тридцать',
            40: 'сорок', 50: 'пятьдесят'}
minuted_dict = {0: 'минут', 1: 'минута', 2: 'минуты', 3: 'минуты', 4: 'минуты'}
min_dict2 = {59: 'одной', 58: 'двух', 57: 'трех', 56: 'четырех', 55: 'пяти', 54: 'шести', 53: 'семи', 52: 'восеми',
             51: 'девяти', 50: 'десяти', 49: 'одиннадцати', 48: 'двенадцати', 47: 'тринадцати', 46: 'четырнадцати',
             45: 'пятнадцати'}
def number_to_words2(num):
    if num < 20 or num % 10 == 0:
        return min_dict.get(num)
    else:
        return f'{min_dict.get(num // 10 * 10)} ' \
               f'{min_dict.get(num % 10)}'
def number_to_words(num):
    if num < 5:
        return minuted_dict.get(num)
    elif 5 <= num < 20:
        return minuted_dict.get(0)
    else:
        return number_to_words(num % 10)
def time_convert(time):
    hour = time.hour
    min = time.minute
    str_time = time.strftime("%H:%M")
    if min == 00:
        if hour == 1 or hour == 13:
            end = ''
        elif hour == 2 or hour == 3 or hour == 4 or hour == 14 or hour == 15 or hour == 16:
            end = 'а'
        else:
            end = 'ов'
        str_time = f'{str_time} - {hour_dict.get(hour)} час{end} ровно'
    elif min < 45 and min != 30:
        str_time = f'{str_time} - {number_to_words2(min)} {number_to_words(min)} {hour_dict2.get(hour + 1)}'
    elif min == 30:
        str_time = f'{str_time} - половина {hour_dict2.get(hour + 1)}'
    elif min >= 45:
        end = 'ы' if min == 59 else ''
        str_time = f'{str_time} - без {min_dict2.get(min)} минут{end} {hour_dict2.get(hour + 1)}'
    return str_time
choice = input("Select the option, get the current time value [current], or enter from the console[input]\n")
if choice == "current":
    current_time = dt.now()
    print(time_convert(current_time))
elif choice == "input":
    input_time = dt.strptime(input("Enter time "), '%H:%M')
    print(time_convert(input_time))
else:
    print('Enter the value again')
