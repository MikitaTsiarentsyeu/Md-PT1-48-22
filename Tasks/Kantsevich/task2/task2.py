from datetime import datetime
HOURS_CASE_1 = {0:'двенадцать часов', 
1:'один час', 2:'два часа',
3:'три часа', 4:'четыре часа',
5:'пять часов', 6:'шесть часов',
7:'семь часов', 8:'восемь часов',
9:'девять часов', 10:'десять часов',
11:'одиннадцать часов'}

HOURS_CASE_2 = {1:'первого', 2:'второго',
3:'третьего', 4:'четвертого',
5:'пятого', 6:'шестого',
7:'седьмого', 8:'восьмого',
9:'девятого', 10:'десятого',
11:'одиннадцатого', 12:'двеннадцатого'}

MINUT_CASE_3 = {1:'одна минута', 2:'две минуты',
3:'три минуты', 4:'четыре минуты',
5:'пять минут', 6:'шесть минут',
7:'семь минут', 8:'восемь минут',
9:'девять минут', 10:'десять минут',
11:'одиннадцать часов', 12:'двенадцать минут',
13:'тринадцать минут', 14:'четырнадцать минут',
15:'пятнадцать минут', 16:'шестнадцать минут',
17:'семнадцать минут', 18:'восемнадцать минут', 19:'девятнадцать минут'}

MINUT_CASE_4 = {20:'двадцать', 30:'тридцать',
40:'сорок'}

HOUR_CASE_5 = {1:'час', 2:'два',
3:'три', 4:'четыре',
5:'пять', 6:'шесть',
7:'семь', 8:'восемь',
9:'девять', 10:'десять',
11:'одиннадцать', 12:'двенадцать'}

MINUT_CASE_6 = {1:'одной минуты', 2:'двух минут',
3:'трех минут', 4:'четырех минут',
5:'пяти минут', 6:'шести минут',
7:'семи минут', 8:'восеми минут',
9:'девяти минут', 10:'десяти минут',
11:'одиннадцати минут', 12:'двенадцати минут',
13:'тринадцати минут', 14:'четырнадцати минут',
15:'пятнадцати минут'}

time = input("Введите время в формате чч:мм, либо нажмите Enter, чтобы узнать текущее время: ")
if time ==(''):
    current_datatime = datetime.now()
    time_to_show = (current_datatime.hour %12,current_datatime.minute)
    print('Текущее время', time_to_show)
else:
    datatime_object = datetime.strptime(time, "%H:%M")
    time_to_show = (datatime_object.hour %12,datatime_object.minute)
    print('Время, веденное пользователем',time_to_show)
    
#min == 0: такое-то значение часа ровно (15:00 - три часа ровно)
#min < 30: столько-то минут следующего часа (19:12 - двенадцать минут восьмого)
#min == 30: половина такого-то (15:30 - половина четвёртого)
#min > 30 and min < 45 столько-то минут следующего часа (12:38 - тридцать восемь минут первого)
#min >= 45 без min такого-то (08:54 - без шести минут девять)

if time_to_show[1]==0:
    print(HOURS_CASE_1[time_to_show[0]]+' ровно')

elif time_to_show[1]==30:
    print('половина '+ HOURS_CASE_2[time_to_show[0]+1])

elif time_to_show[1]<45:
    if time_to_show[1]<20:
        minuts_str = MINUT_CASE_3[time_to_show[1]]
    else:
        minuts_str = MINUT_CASE_4[time_to_show[1] - time_to_show[1] %10] + (' ') + MINUT_CASE_3[time_to_show[1] %10]
    print(minuts_str, HOURS_CASE_2[time_to_show[0]+1])
else:
    print('без ' + MINUT_CASE_6[60-time_to_show[1]] + ' '+ HOUR_CASE_5[time_to_show[0]+1])
