from datetime import datetime



mode = input("Pleas enter mode 1 - current time, 2 - your time:\n")
if mode == "1":
    time = datetime.today().strftime("%I:%M")
else:
    time = input("Enter time format hh:mm:\n")
    time = datetime.strptime(time, "%H:%M").strftime("%I:%M")
hours = int(time.split(":")[0])
minutes = int(time.split(":")[1])
expect = "первого"
hours_zero = {1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь",
                  9: "девять", 10: "десять",11: "одинадцать",12: "двенадцать"}
hours_half = {1: "первого", 2: "второго", 3: "третьего", 4: "четвертогое", 5: "пятого", 6: "шестого", 7: "седьмого",
              8: "восьмого", 9: "девятого", 10: "десятого",11: "одинадцатого",12: "двенадцатого"}
minute = {1: "одна", 2: "две", 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять",
          10: "десять", 11: "одинадцать", 12: "двенадцать", 13: "тренадцать", 14: "четырнадцать", 15: "пятнадцать",
          16: "шеснадцать", 17: "семнадцать", 18: "восемнадцать", 19: "девятнадцать", 20: "двадцать", 30: "тридцать",
          40: "сорок", 50: "пятьдесят"}
if minutes == 0:
    if 1 < hours <= 4:
        print(f"{hours_zero.get(hours)} часа ровно")
    elif 4 < hours <= 12:
        print(f"{hours_zero.get(hours)} часов ровно")
    else:
        print(f"{hours_zero.get(hours)} час ровно")

elif minutes < 30:
    if 1 < hours <= 12:
        if minutes == 1:
            print(f"{minute.get(minutes)} минута {hours_half.get(hours + 1, expect)}")
        elif 1 < minutes <= 4:
            print(f"{minute.get(minutes)} минуты {hours_half.get(hours + 1, expect)}")
        elif minutes // 10 == 2 and 1 < minutes % 10 <= 4:
            print(f"{minute.get(20)} {minute.get(minutes % 10)} минуты {hours_half.get(hours + 1, expect)}")
        elif minutes // 10 == 2 and 4 < minutes % 10 <= 9:
            print(f"{minute.get(20)} {minute.get(minutes % 10)} минут {hours_half.get(hours + 1, expect)}")
        elif minutes // 10 == 2 and minutes % 10 == 1:
            print(f"{minute.get(20)} {minute.get(minutes % 10)} минута {hours_half.get(hours + 1, expect)}")
        else:
            print(f"{minute.get(minutes)} минут {hours_half.get(hours + 1, expect)}")

elif minutes == 30:
    print(f"Половина {hours_half.get(hours + 1, expect)}")

elif minutes > 30 and minutes < 45:
    if minutes // 10 == 3 and 1 < minutes % 10 <= 4:
        print(f"{minute.get(30)} {minute.get(minutes % 10)} минуты {hours_half.get(hours + 1, expect)}")
    elif minutes // 10 == 3 and 4 < minutes % 10 <= 9:
        print(f"{minute.get(30)} {minute.get(minutes % 10)} минут {hours_half.get(hours + 1, expect)}")
    elif minutes // 10 == 3 and minutes % 10 == 1:
        print(f"{minute.get(30)} {minute.get(minutes % 10)} минута {hours_half.get(hours + 1, expect)}")
    elif minutes // 10 == 4 and 1 < minutes % 10 <= 4:
        print(f"{minute.get(40)} {minute.get(minutes % 10)} минуты {hours_half.get(hours + 1, expect)}")
    elif minutes // 10 == 4 and 4 < minutes % 10 <= 5:
        print(f"{minute.get(40)} {minute.get(minutes % 10)} минут {hours_half.get(hours + 1, expect)}")
    elif minutes // 10 == 4 and minutes % 10 == 1:
        print(f"{minute.get(40)} {minute.get(minutes % 10)} минута {hours_half.get(hours + 1, expect)}")
    else:
        print(f"{minute.get(40)} минут {hours_half.get(hours + 1, expect)}")

else:
    print(f"без {minute.get(60 - minutes)} минут {hours_half.get(hours + 1, expect)}")