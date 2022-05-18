import datetime
question = input("Гость, чего же пожелаешь сейчас?:\n1. Узнать текущее время\n2. Ввести своё время\n")
if question == '1':
    now_time = datetime.datetime.today().strftime("%H:%M")
    hour = int(datetime.datetime.today().strftime("%I"))
    minutes = int(datetime.datetime.today().strftime("%M"))
    question = now_time
elif question == '2':
    question = input('Введи угодное тебе время в формате ЧЧ:ММ\n')
    while True:
        question = input('Введи угодное тебе время в формате ЧЧ:ММ\n')
        if question.split(':')[0].isdigit():
            if question.split(':')[1].isdigit():
                if -1 < int(question.split(':')[0]) < 24:
                    if -1 < int(question.split(':')[1]) < 60:
                        break
    time_user = question.split(':')
    hour_user =int(time_user[0])
    minutes = int(time_user[1])
    now_time = question
    if hour_user > 12:
        hour = hour_user-12
    else:
        hour = hour_user
hour_db = { 1: "один", 2: "два", 3: "три", 4:"четыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять", 10: "десять", 11: "одинадцать", 12: "двенадцать", 0: "ноль"}
hour_db_end = { 1: "час", 2: "два", 3: "три", 4:"четыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять", 10: "десять", 11: "одинадцать", 12: "двенадцать", 0: "двенадцать"}
hour_db_12 = {0: "первого", 1: "второго", 2: "третьего", 3: "четвёртого", 4: "пятого", 5: "шестого", 6: "седьмого", 7: "восьмого", 8: "девятого", 9: "десятого", 10: "одинадцатаго", 11: "двенадцатого", 12: "первого"}
minutes_db = {0: "ноль", 1: "одна", 2: "две", 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять", 10: "десять", 11: "одинадцать", 12: "двенадцать", 13: "тринадцать", 14: "четырнадцать", 15: "пятнадцать", 16: "шестьнадцать", 17: "семьнадцать", 18: "восемьнадцать", 19: "девятнадцать", 20: "двадцать", 30: "тридцать", 40: "сорок", 45: "пятнадцати", 46: "четырнадцати", 47: "тринадцати", 48: "двенадцати", 49: "одиннадцати", 50: "десяти", 51: "девяти", 52: "восьми", 53: "семи", 54: "шести", 55: "пяти", 56: "четырех", 57: "трех", 58: "двух", 59: "одной"}
names_hours = {1: "час", 2: "часа", 3: "часов"}
names_minutes = {1: "минут", 2: "минуты", 3: "минута"}
minutes_ones = minutes%10
minutes_tens = minutes-minutes_ones
if 4 < minutes < 21:
    name_minutes = 1
elif minutes_ones > 4:
    name_minutes = 1
elif minutes_ones == 1:
    name_minutes = 3
else:
    name_minutes = 2

if minutes == 0:
    if hour == 1:
        name_hour = 1
    elif hour > 4:
        name_hour = 3
    elif hour < 1:
        name_hour = 3
    else:
        name_hour = 2
    print(question, '-', hour_db[hour], names_hours[name_hour], 'ровно')
elif minutes < 20:
    print(question, '-', minutes_db[minutes], names_minutes[name_minutes], hour_db_12[hour])
elif minutes ==30:
    print(question, '- половина', hour_db_12[hour])
elif minutes > 44:
    if minutes_ones == 1:
        name_minutes = 2
    else:
        name_minutes = 1
    print(question, '- без', minutes_db[minutes], names_minutes[name_minutes], hour_db_end[hour])
else:
    if minutes_ones == 0:
        print(question, '-', minutes_db[minutes_tens], names_minutes[name_minutes], hour_db_12[hour])
    else:
        print(question, '-', minutes_db[minutes_tens], minutes_db[minutes_ones], names_minutes[name_minutes], hour_db_12[hour])