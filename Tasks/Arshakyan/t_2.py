import datetime

h_dict = {1:[("один", "первого")], 2:[("два", "второго")], 3:[("три", "третьего")], 4:[("четыре", "четвертого")],
5:[("пять", "пятого")], 6:[("шесть", "шестого")], 7:[("семь", "седьмого")], 8:[("восемь", "восьмого")],
9:[("девять", "девятого")], 10:[("десять", "десятого")], 11:[("одиннадцать", "одиннадцатого")], 
12:[("двенадцать", "двенадцатого")], 0:[("ноль","двенадцатого")]}
m_dict = {1:[("одна", "одной")], 2:[("две", "двух")], 3:[("три", "трех")], 4:[("четыре", "четырёх")], 5:[("пять", "пяти")],
6:[("шесть", "шести")], 7:[("семь", "семи")], 8:[("восемь", "восьми")], 9:[("девять", "девяти")], 10:[("десять", "десяти")],
11:[("одиннадцать", "одиннадцати")], 12:[("двенадцать", "двенадцати")], 13:[("тринадцать", "тринадцати")], 
14:[("четырнадцать", "четырнадацати")], 15:[("пятнадцать", "пятнадцати")], 16: [("шестнадцать")], 17:[("семнадцать")],
18:[("восемнадцать")], 19:[("девятнадцать")], 20:[("двадцать")], 21:[("двадцать одна")], 22:[("двадцать две")],
23:[("двадцать три")], 24:[("двадцать четыре")], 25:[("двадцать пять")], 26:[("двадцать шесть")], 27:[("двадцать семь")],
28:[("двадцать восемь")], 29:[("двадцать девять")], 30:[("половина")], 31:[("тридцать одна")], 32:[("тридцать две")],
33:[("тридцать три")], 34:[("тридцать четыре")], 35:[("тридцать пять")], 36:[("тридцать шесть")], 37:[("тридцать семь")],
38:[("тридцать восемь")], 39:[("тридцать девять")], 40:[("сорок")], 41:[("сорок одна")], 42:[("сорок две")], 43:[("сорок три")], 44:[("сорок четыре")], 00:[("ровно")]}
min_name = {1: "минута", 2: "минуты", 3: "минут"}

main = (input("Введите время в виде hh:mm, формата 24 часа, если время не выбрано, программа выведет текущее время:\n"))
if ((len(main) != 5) or (int((main[:2])) > 23) or (int((main[3:])) > 59) or (main[2] != ':')):
    main = datetime.datetime.now().strftime("%H:%M")
    print("Текущее время:")

hour = int(main[:2])
min =  int(main[3:])
if hour >= 12:
    hour = hour - 12
else:
    hour = hour
min_1 = min % 10
min_10 = min - min_1
if 4 < min < 21:
    name = 3
elif 1 < min_1 < 5:
    name = 2
elif min_1 == 1:   
    name = 1
elif min == 59:
    name = 2
else:
    name = 3
if min == 0:
    if hour == 1:
        print(f'{h_dict[hour][0][0]} час {m_dict[0]}')
    elif 1 < hour < 5:
        print(f'{h_dict[hour][0][0]} часа {m_dict[0]}')
    else:
        print(f'{h_dict[hour][0][0]} часов {m_dict[0]}')
elif min == 30:
    print(f'{m_dict[min][0]} {h_dict[hour+1][0][1]}')
elif 0 < min < 16:
    print(f'{m_dict[min][0][0]} {min_name[name]} {h_dict[hour+1][0][1]}')
elif min >= 45:
    min = 60 - min
    print(f'без {m_dict[min][0][1]} {min_name[name]} {h_dict[hour+1][0][0]}')
else:
    print(f'{m_dict[min][0]} {min_name[name]} {h_dict[hour+1][0][1]}')
