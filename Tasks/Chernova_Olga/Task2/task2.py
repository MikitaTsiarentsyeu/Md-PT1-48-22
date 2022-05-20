from datetime import datetime

now_time = input('Укажите время в формате ЧЧ:ММ, в ином случае \
время будет определено автоматически: ')

if ((len(now_time) != 5) or (int((now_time[:2])) > 23) or (int((now_time[3:])) > 59) 
or (now_time[2] != ':')):
    now_time = str(datetime.now().time())[:5]
    print("Данные введены неверно, будет использовано текущее время")

min_numbers = {1:(("одна","одной"),("десять ","десяти"),("одинадцать","одинадцати"))}
min_numbers[2] = (("две","двух"),("двадцать ",''),("двенадцать","двенадцати"))
min_numbers[3] = (("три","трёх"),("тридцать ",''),("тринадцать","тринадцати"))
min_numbers[4] = (("четыре","четырёх"),("сорок ",''),("четырнадцать","четырнадцати"))
min_numbers[5] = (("пять","пяти"),(),("пятнадцать","пятнадцати"))
min_numbers[6] = (("шесть","шести"),(),("шестнадцать",''))
min_numbers[7] = (("семь","семи"),(),("семнадцать",''))
min_numbers[8] = (("восемь","восьми"),(),("восемнадцать",''))
min_numbers[9] = (("девять","девяти"),(),("девятнадцать",''))
min_numbers[0] = (('',''),('',''),())

hour_number = {1:("один","первого")}
hour_number[2] = ("два","второго")
hour_number[3] = ("три","третьего")
hour_number[4] = ("четыре","четвертого")
hour_number[5] = ("пять","пятого")
hour_number[6] = ("шесть","шестого")
hour_number[7] = ("семь","седьмого")
hour_number[8] = ("восемь","восьмого")
hour_number[9] = ("девять","девятого")
hour_number[10] = ("десять","десятого")
hour_number[11] = ("одинадцать","одинадцатого")
hour_number[12] = ("двенадцать","двенадцатого")

hours = int(now_time[:2])
minutes =  int(now_time[3:])

if hours >= 12:
    hours = hours - 12

if minutes == 0:
    if hours == 0:
        print(f'{now_time} - {hour_number[hours+12][0]} часов ровно')
    elif hours == 1 :
        print(f'{now_time} - {hour_number[hours][0]} час ровно')
    elif hours < 5 :
        print(f'{now_time} - {hour_number[hours][0]} часа ровно')
    else:
        print(f'{now_time} - {hour_number[hours][0]} часов ровно')
elif minutes == 30:
    print(f'{now_time} - половина {hour_number[hours+1][1]}')
elif minutes >= 45:
    if 60-minutes ==1:
        print(f'{now_time} - без {min_numbers[1][0][1]} минуты {hour_number[hours+1][0]}')
    elif 60-minutes ==10:
        print(f'{now_time} - без {min_numbers[1][1][1]} минут {hour_number[hours+1][0]}')
    elif 60-minutes < 10:
        print(f'{now_time} - без {min_numbers[60-minutes][0][1]} минут {hour_number[hours+1][0]}')
    else:
        print(f'{now_time} - без {min_numbers[60-minutes-10][2][1]} минут {hour_number[hours+1][0]}')
else:
    if minutes % 10 == 1 and minutes != 11:
        print(f'{now_time} - {min_numbers[minutes // 10][1][0]}{min_numbers[minutes % 10][0][0]} минута {hour_number[hours+1][1]}')
    elif minutes % 10 < 5 and minutes not in range (11,15):
        print(f'{now_time} - {min_numbers[minutes // 10][1][0]}{min_numbers[minutes % 10][0][0]} минуты {hour_number[hours+1][1]}')
    elif minutes in range (11,20):
        print(f'{now_time} - {min_numbers[minutes % 10][2][0]} минут {hour_number[hours+1][1]}')
    else:
        print(f'{now_time} - {min_numbers[minutes // 10][1][0]}{min_numbers[minutes % 10][0][0]} минут {hour_number[hours+1][1]}')