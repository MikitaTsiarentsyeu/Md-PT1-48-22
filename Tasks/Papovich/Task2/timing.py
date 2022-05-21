import datetime
choose_time = input("Выбери вариант\n1.текущеее время\n2 ваше время\n")
if choose_time == '1':
    current_time = datetime.datetime.now().strftime("%H:%M")
    hours = int(datetime.datetime.now().strftime("%H"))
    minutes = int(datetime.datetime.now().strftime("%M"))
elif choose_time == '2':
    choose_time = input("введите ваше время HH:MM\n")
    time_user = choose_time.split(":")
    hours = int(time_user[0])
    minutes = int(time_user[1])
    current_time = choose_time
print(current_time)
hours_1 = {0: "ноль", 1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять", 10: "десять", 11: "одиннадцать", 12: "двенадцать", 13: "тринадцать", 14: "четырнадцать", 15: "пятнадцать", 16: "шестнадцать", 17: "семнадцать", 18: "восемнадцать", 19: "девятнадцать", 20: "двадцать", 21: "двадцать один", 22: "двадцать два", 23: "двадцать три", 24: "двадцать четыре"}
hours_2 = {0: "первого", 1: "второго", 2: "третьего", 3: "четвертого", 4: "пятого", 5: "шестого", 6: "седьмого", 7: "восьмого", 8: "девятого", 9: "десятого", 10: "одиннадцатого", 11: "двенадцатого", 12: "первого", 13: "втогоро", 14: "третьего", 15: "четвертого", 16: "пятого", 17: "шестого", 18: "седьмого", 19: "восьмого", 20: "девятого", 21: "десятого", 22: "одиннадцатого", 23: "двенадцатого"}
hours_names = {1: "час", 2: "часа", 3: "часов"}
minute_dictionary = {0: "ноль", 1: "одна", 2: "две", 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять", 10: "десять", 11: "одиннадцать", 12: "двенадцать", 13: "тринадцать", 14: "четырнадцать", 15: "пятнадцать", 16: "шестнадцать", 17: "семнадцать", 18: "восемнадцать", 19: "девятнадцать", 20: "двадцать", 30: "тридцать", 40: "сорок", 45: "пятнадцати", 46: "четырнадцати", 47: "тринадцати", 48: "двенадцати", 49: "одинадцати",  50: "десяти", 51: "девяти", 52: "восьми", 53: "семи", 54: "шести", 55: "пяти", 56: "четырех", 57: "трех", 58: "двух", 59: "одной"}
minute_dictionary_names = {1: "минут", 2: "минуты", 3: "минута"}
minutes_1 = minutes%10
minutes_10 = minutes - minutes_1
if 4 < minutes < 21:
    name_minutes = 1
elif minutes_1 > 4:
    name_minutes = 2
elif minutes_1 == 1:   
    name_minutes = 3 
else:
    name_minutes = 2 
if minutes == 0:
    if hours == 1:
        name_hour = 1
    if hours == 21:
        name_hour = 1
    elif 22 <= hours <= 24:
        name_hour = 2
    elif hours > 4:
        name_hour = 3
    elif hours < 1:
        name_hour = 3
    else:
        name_hour = 2
    print(hours_1[hours], hours_names[name_hour], "ровно")
elif minutes < 20:
    print(minute_dictionary[minutes], minute_dictionary_names[name_minutes], hours_2[hours])
elif minutes == 30:
        print("половина", hours_2[hours])
elif minutes > 44:
    if minutes_1 == 1:
        name_minutes = 2 
    else:
        name_minutes = 1
    print("без", minute_dictionary[minutes], minute_dictionary_names[name_minutes], hours_2[hours])
else:
    if minutes_1 == 0:
        print(minute_dictionary[minutes_10], minute_dictionary_names[name_minutes], hours_2[hours])
    else:
        print(minute_dictionary[minutes_10], minute_dictionary[minutes_1], minute_dictionary_names[name_minutes], hours_2[hours])