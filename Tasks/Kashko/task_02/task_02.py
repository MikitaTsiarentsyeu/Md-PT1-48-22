from datetime import datetime

HOURS = [['один', 'первого', 'час'], ['два', 'второго', 'часа'],
         ['три', 'третьего', 'часа'], ['четыре', 'четвертого', 'часа'],
         ['пять', 'пятого', 'часов'], ['шесть', 'шестого', 'часов'],
         ['семь', 'седьмого', 'часов'], ['восемь', 'восьмого', 'часов'],
         ['девять', 'девятого', 'часов'], ['десять', 'десятого', 'часов'],
         ['одиннадцать', 'одиннадцатого', 'часов'],
         ['двенадцать', 'двенадцатого', 'часов']]

MINUTES = {
    1: ['одна', 'одной', 'минута', 'минуты'],
    2: ['две', 'двух', 'минуты', 'минут'],
    3: ['три', 'трех', 'минуты', 'минут'],
    4: ['четыре', 'четырех', 'минуты', 'минут'],
    5: ['пять', 'пяти', 'минут', 'минут'],
    6: ['шесть', 'шести', 'минут', 'минут'],
    7: ['семь', 'семи', 'минут', 'минут'],
    8: ['восемь', 'восьми', 'минут', 'минут'],
    9: ['девять', 'девяти', 'минут', 'минут'],
    10: ['десять', 'десяти', 'минут', 'минут'],
    11: ['одиннадцать', 'одиннадцати', 'минут', 'минут'],
    12: ['двенадцать', 'двенадцати', 'минут', 'минут'],
    13: ['тринадцать', 'тринадцати', 'минут', 'минут'],
    14: ['четырнадцать', 'четырнадцати', 'минут', 'минут'],
    15: ['пятнадцать', 'пятнадцати', 'минут', 'минут'],
    16: ['шестнадцать', 'шестнадцати', 'минут', 'минут'],
    17: ['семнадцать', 'семнадцати', 'минут', 'минут'],
    18: ['восемнадцать', 'восемнадцати', 'минут', 'минут'],
    19: ['девятнадцать', 'девятнадцати', 'минут', 'минут'],
    20: ['двадцать', 'двадцати', 'минут', 'минут'],
    30: ['тридцать', 'тридцати', 'минут', 'минут'],
    40: ['сорок', 'сорока', 'минут', 'минут'],
}


def input_time() -> datetime:
    """Reads user input and returns time as datetime object.

    Input time in format: HH:MM or empty string to get current time.

    Returns:
        datetime: datetime object
    """
    while True:

        try:
            user_time = input('Enter time as HH:MM\n')
            if user_time == '':
                user_time = datetime.now()
                break
            user_time = datetime.strptime(user_time, '%H:%M')
            break

        except ValueError as error:
            print(f'Invalid time format: {error}')

    return user_time


def time_to_text(time: datetime) -> str:
    """Represents datetime object as words in Russian
    and returns time in text format.

    Args:
        time (datetime): datetime object to convert

    Returns:
        str: string with time as words
    """
    text_time = time.strftime("%H:%M")

    if time.hour >= 12:
        h = time.hour - 12
    else:
        h = time.hour
    m = time.minute

    if m == 0:
        text = f"{text_time} - {HOURS[h-1][0]} " \
               f"{HOURS[h-1][2]} ровно"
    elif m <= 20:
        text = f"{text_time} - {MINUTES[m][0]} " \
               f"{MINUTES[m][2]} {HOURS[h][1]}"
    elif m == 30:
        text = f"{text_time} - половина {HOURS[h][1]}"
    elif m >= 45:
        text = f"{text_time} - без {MINUTES[60-m][1]} " \
               f"{MINUTES[60-m][3]} {HOURS[h][0]}"
    else:
        if not m % 10:
            text = f"{text_time} - {MINUTES[m][0]} " \
                   f"{MINUTES[m][2]} {HOURS[h][1]}"
        else:
            text = f"{text_time} - {MINUTES[(m // 10)*10][0]} " \
               f"{MINUTES[m % 10][0]} {MINUTES[m % 10][2]} {HOURS[h][1]}"

    return text


if __name__ == '__main__':
    print(time_to_text(input_time()))
