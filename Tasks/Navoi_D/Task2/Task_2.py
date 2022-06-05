
import datetime

MinMoreQuarter = {45:"пятнадцати", 46:"четырнадцати", 47:"тринадцати", 48:"двенадцати", 49:"одиннадцати", 50:" десяти", 51:"девяти", 
            52:" восьми", 53:"семи", 54:"шести", 55:"пяти", 56:"четырех", 57:"трех", 58:" двух", 59:"одной"}
HoursZero = {0:"двенадцать ночи", 1:"час ночи", 2:"два часа ночи", 3:"три часа ночи", 4:"четыре часа утра", 5:"пять часов утра", 
            6:"шесть часов утра",7:"семь часов утра", 8:"восемь часов утра", 9:"девять часов утра", 10:"десять часов утра", 
            11:"одинадцать часов утра", 12:"двенадцать дня", 13:"час дня", 14:"два часа дня", 15:"три часа дня", 
            16:"четыре часа вечера", 17:"пять часов вечера", 18:" шесть часов вечера", 19:"семь вечера", 20:"восемь вечера", 
            21:"девять вечера", 22:"десять вечера", 23:"одинадцать вечера", 24:"двенадцать ночи"}
HoursHalf1 = {0:"первого ночи", 1:"второго ночи", 2:"третьего ночи", 3:"четвертого утра", 4:"пятого утра", 5:"шестого утра", 6:"седьмого утра",
             7:"восьмого утра", 8:"девятого утра", 9:"десятого утра", 10:"одинадцатого утра", 11:"двенадцатого дня", 12:"первого дня",
            13:"второго дня", 14:"третьего дня", 15:"четвертого вечера", 16:"пятого вечера", 17:"шестого вечера", 18:"седьмого вечера", 
            19:"восьмого вечера", 20:"девятого вечера", 21:"десятого вечера", 22:"одинадцатого вечера", 23:"двенадцатого ночи"}
MinUnderHalf = {1:"одна минута", 2:"две минуты", 3:"три минуты", 4:"четыре минуты", 5:"пять минут", 6:"шесть минут", 7:"семь минут",
            8:"восемь минут", 9:"девять минут", 10:"десять минут", 11:"одинадцать минут", 12:"двенадцать минут", 13:"тринадцать минут",
            14:"четырнадцать минут", 15:"четверть", 16:"шестнадцать минут", 17:"семнадцать минут", 18:"восемнадцать минут", 
            19:"девятнадцать минут", 20:"двадцать минут", 21:"двадцать одна минута", 22:"двадцать две минуты", 23:"двадцать три минуты", 
            24:"двадцать четыре минуты", 25:"двадцать пять минут", 26:"двадцать шесть минут", 27:"двадцать семь минут", 28:"двадцать восемь минут",
            29:"двадцать девять минут"}
MinHalfQuarter = {31:"тридацать одна минута", 32:"тридцать две минуты", 33:"тридцать три минуты", 34:"тридцать четыре минуты", 
            35:"тридцать пять минут", 36:"тридцать шесть минут", 37:"тридцать семь минут", 38:"тридцать восемь минут",
            39:"тридцать девять минут", 40:"сорок минут", 41:"сорок одна минута", 42:"сорок две минуты", 43:"сорок три минуты",
            44:"сорок четыре минуты"}

a = int(input(" Здравствуйте! Выберите режим работы программы! \n Если вы хотите узнать текущее время введите цифру 1 \n Если вы хотите ввести время с клавиатуры введите цифру 2 \n" ))
if a == 1 or a == 2: 
   
    # получение текущего времени
    if a == 1:
        Hours = datetime.datetime.today().time().hour
        Minutes = datetime.datetime.today().time().minute
        today = datetime.datetime.today()
        Time_Numbers = today.strftime("%H:%M")

    # ввод времени пользователем
    else:
        time_entry = input("введите время в формате ЧЧ:ММ (цифру 24 не использовать, только 0) \n") 
        Hours, Minutes = map(int, time_entry.split(':')) 
        Time1 = datetime.time(Hours, Minutes) 
        Time_Numbers = (str(Time1).rsplit(':', 1)[0])   
    
    # проверка условий
    if Minutes == 0:
        print(Time_Numbers, HoursZero[Hours]) 
    if Minutes < 30 and Minutes > 0:
        print(Time_Numbers, f"{MinUnderHalf[Minutes]} {HoursHalf1[Hours]}")
    if Minutes == 30:
        print(Time_Numbers, f"половина {HoursHalf1[Hours]}")
    if Minutes > 30 and Minutes < 45:
        print(Time_Numbers, f"{MinHalfQuarter[Minutes]} {HoursHalf1[Hours]} ") 
    if Minutes >= 45:
        if Minutes >= 45 and Minutes < 59:
            print(Time_Numbers, f"без {MinMoreQuarter[Minutes]} минут {HoursZero[Hours+1]}")
        elif Minutes == 59:
            print(Time_Numbers, f"без {MinMoreQuarter[Minutes]} минуты {HoursZero[Hours+1] }") 
else:
    print("Вы ввели неверные цифры, перезапустите программу") 
    