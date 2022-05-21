import datetime

time_naming_dict = {
    1: [
        'один', 'первого', 'одной', 'одна',
    ],
    2: [
        'два', 'второго', 'двух', 'две',
    ],
    3: [
        'три', 'третего', 'трех',
    ],
    4: [
        'четыре', 'четвертого', 'четырех',
    ],
    5: [
        'пять', 'пятого', 'пяти',
    ],
    6: [
        'шесть', 'шестого', 'шести',
    ],
    7: [
        'семь', 'седьмого', 'семи',
    ],
    8: [
        'восемь', 'восьмого', 'восьми',
    ],
    9: [
        'девять', 'девятого', 'девяти',
    ],
    10: [
        'десять', 'девятого', 'десяти',
    ],
    11: [
        'одинадцать', 'одинадцатого', 'одинадцати',
    ],
    12: [
        'двенадцать', 'двенадцатого', 'двенадцати',
    ],
    13: [
        'тринадцать', 'тринадцатого', 'тринадцати',
    ],
    14: [
        'четырнадцать', 'четырнадцатого', 'четырнадцати',
    ],
    15: [
        'пятнадцать', 'пятнадцатого', 'пятнадцати',
    ],
    16: ['шестнадцать',],
    17: ['семнадцать',],
    18: ['восемнадцать',],
    19: ['девятнадцать',],

    20: ['двадцать',],
    30: ['тридцать',],
    40: ['сорок',],
    50: ['пятьдесят',],
}


def get_hours_and_minutes_from_input():
    input_time = input("Type time in format HH:MM \nor leave empty to get time now\n")

    if input_time == '':
        input_time = datetime.datetime.now().strftime("%H:%M")

    hours, minutes = input_time.split(':')

    hours, minutes = int(hours), int(minutes)
    # hours = hours if hours < 13 else hours - 12

    return (hours, minutes)


def get_minutes_naming_from_1_to_44(minutes):
    str_num_minutes = ''
    tmp_min_1, tmp_min_2 = (minutes//10)*10, minutes%10

    if minutes < 3:
        # diferent spellind for 1, 2
        str_num_minutes = time_naming_dict[minutes][3]
    elif minutes < 20:
        # get values for (4 .. 19) from dictionary
        str_num_minutes = time_naming_dict[minutes][0]
    else:
        if tmp_min_2 == 0:
            # number ends on 0
            str_num_minutes = f"{time_naming_dict[tmp_min_1][0]}"
        else:
            # numbers which concatinates from 2 parts
            str_num_minutes = f"{time_naming_dict[tmp_min_1][0]} {time_naming_dict[tmp_min_2][3] if tmp_min_2 < 3 else time_naming_dict[tmp_min_2][0]}"
    
    return str_num_minutes


def get_spelled_time(hours, minutes):

    hours = hours if minutes == 0 else hours+1

    hours = hours%12
    hours = 12 if hours == 0 else hours

    if minutes == 0:
        # min == 0: такое-то значение часа ровно (15:00 - три часа ровно)
        tmp_hours = ''

        if hours == 1:
            tmp_hours = 'час'
        elif hours < 5:
            tmp_hours = 'часа'
        else:
            tmp_hours = 'часов'
        
        return f"{time_naming_dict[hours][0]} {tmp_hours} ровно"

    elif minutes == 30:
        # min == 30: половина такого-то (15:30 - половина четвёртого)
        return f"половина {time_naming_dict[hours][1]}"

    elif minutes > 44:
        # min >= 45 без min такого-то (08:54 - без шести минут девять)
        minutes = 60 - minutes
        str_minutes = None

        if minutes == 1:
            str_minutes = 'минуты'
        else:
            str_minutes = 'минут'

        return f"без {time_naming_dict[minutes][2]} {str_minutes} {'час' if hours == 1 else time_naming_dict[hours][0]}"
    
    else:    
        tmp_min_1, tmp_min_2 = minutes//10, minutes%10
        if tmp_min_2 == 1 and tmp_min_1 != 1:
            str_minutes = 'минута'
        elif tmp_min_2 in (2, 3, 4) and tmp_min_1 != 1:
            str_minutes = 'минуты'
        else:
            str_minutes = 'минут'

        str_num_minutes = get_minutes_naming_from_1_to_44(minutes)
        return f"{str_num_minutes} {str_minutes} {time_naming_dict[hours][1]}"


if __name__ == '__main__':
    hours, minutes = get_hours_and_minutes_from_input()
    solution_str = get_spelled_time(hours, minutes)
    print(solution_str)
