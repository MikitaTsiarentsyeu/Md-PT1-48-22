import datetime

time_dict = {0: ["ноль", "часов", "", "", ""],
             1: ["один", "час", "первого", "одна минута", "одной минуты"],
             2: ["два", "часа", "второго", "две минуты", "двух минут"],
             3: ["три", "часа", "третьего", "три минуты", "трёх минут"],
             4: ["четыре", "часа", "четвёртого", "четыре минуты", "четырёх минут"],
             5: ["пять", "часов", "пятого", "пять минут", "пяти минут"],
             6: ["шесть", "часов", "шестого", "шесть минут", "шести минут"],
             7: ["семь", "часов", "седьмого", "семь минут", "семи минут"],
             8: ["восемь", "часов", "восьмого", "восемь минут", "восьми минут"],
             9: ["девять", "часов", "девятого", "девять минут", "девяти минут"],
             10: ["десять", "часов", "десятого", "десять минут", "десяти минут"],
             11: ["одиннадцать", "часов", "одиннадцатого", "одиннадцать минут", "одиннадцати минут"],
             12: ["двенадцать", "часов", "двенадцатого", "двенадцать минут", "двенадцати минут"],
             13: ["", "", "", "тринадцать минут", "тринадцати минут"],
             14: ["", "", "", "четырнадцать минут", "четырнадцати минут"],
             15: ["", "", "", "пятнадцать минут", "пятнадцати минут"],
             16: ["", "", "", "шестнадцать минут"],
             17: ["", "", "", "семнадцать минут"],
             18: ["", "", "", "восемнадцать минут"],
             19: ["", "", "", "девятнадцать минут"],
             20: ["двадцать", "", "", "двадцать минут"],
             30: ["тридцать", "", "", "тридцать минут"],
             40: ["сорок", "", "", "сорок минут"]}


def time_conversion(time):
    hour, minute = time.split(":")
    hour_int, minute_int = int(hour), int(minute)

    if hour_int >= 12:
        hour_int -= 12

    if minute_int == 0:
        return f"{hour}:{minute} - {time_dict[hour_int][0]} {time_dict[hour_int][1]} ровно"
    elif minute_int == 30:
        return f"{hour}:{minute} - половина {time_dict[hour_int + 1][2]}"
    elif 0 < minute_int < 45:
        if minute_int <= 20 or minute_int == 30 or minute_int == 40:
            return f"{hour}:{minute} - {time_dict[minute_int][3]} {time_dict[hour_int + 1][2]}"
        elif 20 < minute_int < 45:
            first_number = int(minute[0]) * 10
            return f"{hour}:{minute} - {time_dict[first_number][0]} {time_dict[int(minute[1])][3]} {time_dict[hour_int + 1][2]}"
    elif minute_int >= 45:
        rest = 60 - minute_int
        return f"{hour}:{minute} - без {time_dict[rest][4]} {time_dict[hour_int + 1][0]}"


current_date = datetime.datetime.now()
option = input("What do you want to do:\n 1 - display the current time\n 2 - display time from console\n")

if option == "1":
    print(time_conversion(current_date.strftime("%H:%M")))
elif option == "2":
    while True:  # checking the entered value for conformity to the format
        input_time = input("Enter the time in the format HH:MM: ")
        if len(input_time) > 5:
            print("Repeat input (too long value)")
        elif len(input_time) < 5:
            print("Repeat input (too short value)")
        elif input_time[2] != ":":
            print("Repeat input (must be a character ':')")
        elif not input_time.split(":")[0].isdigit() or not 0 <= int(input_time.split(":")[0]) < 24:
            print("Repeat input ('HH' must consist of numbers from 0 to 23)")
        elif not input_time.split(":")[1].isdigit() or not 0 <= int(input_time.split(":")[1]) < 60:
            print("Repeat input ('MM' must consist of numbers from 0 to 59)")
        else:
            break
    print(time_conversion(input_time))
else:
    print("Wrong input")
