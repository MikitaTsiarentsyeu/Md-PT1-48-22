Task2
2.1.
import pytz
import datetime

tz_minsk = pytz.timezone("Europe/Minsk")
dt_minsk =datetime.datetime.now(tz_minsk)
dt_minsk_string = dt_minsk.strftime('%H:%M:%S')

print('Текущее время : ',dt_minsk_string)





2.2.
hour = int(input("Укажите пожалуйста который сейчас час в 12-часовом формате? "))
min = int(input("Сколько минут? "))



if min == 0 and hour ==1 :
        print(f"{hour}:{min} - ровно час")

elif min == 0 and hour ==2 :
        print(f"{hour}:{min} - ровно два часа")

elif min == 0 and hour ==3 :
        print(f"{hour}:{min} - ровно три часа")

elif min == 0 and hour ==4 :
        print(f"{hour}:{min} - ровно четыре часа")

elif min == 0 and hour ==5 :
        print(f"{hour}:{min} - ровно пять часов")

elif min == 0 and hour ==6 :
        print(f"{hour}:{min} - ровно шесть часов")

elif min == 0 and hour ==7 :
        print(f"{hour}:{min} - ровно семь часов")

elif min == 0 and hour ==8 :
        print(f"{hour}:{min} - ровно восемь часов")

elif min == 0 and hour ==9 :
        print(f"{hour}:{min} - ровно девять часов")

elif min == 0 and hour ==10 :
        print(f"{hour}:{min} - ровно десять часов")

elif min == 0 and hour ==11 :
        print(f"{hour}:{min} - ровно одиннадцать часов")

elif min == 0 and hour ==12 :
        print(f"{hour}:{min} - ровно двеннадцать часов")


elif min < 30:
    	     print("Интересное время, которое я не смог распознать")
		

elif min == 30 and hour ==1 :
    		     print(f"{hour}:{min} - половина второго")
elif min == 30 and hour ==2 :
    		     print(f"{hour}:{min} - половина третьего")
elif min == 30 and hour ==3 :
    		     print(f"{hour}:{min} - половина четвертого")
elif min == 30 and hour ==4 :
    		     print(f"{hour}:{min} - половина пятого")	
elif min == 30 and hour ==5 :
    		     print(f"{hour}:{min} - половина шестого")
elif min == 30 and hour ==6 :
    		     print(f"{hour}:{min} - половина седьмого")
elif min == 30 and hour ==7 :
    		     print(f"{hour}:{min} - половина восьмого")
elif min == 30 and hour ==8 :
    		     print(f"{hour}:{min} - половина девятого")	
elif min == 30 and hour ==9 :
    		     print(f"{hour}:{min} - половина десятого")	
elif min == 30 and hour ==10 :
    		     print(f"{hour}:{min} - половина одиннадцатого")	
elif min == 30 and hour ==11 :
    		     print(f"{hour}:{min} - половина двеннадцатого")	



elif min > 30 and min <45:
     print("Интересное время, которое я не смог распознать")
elif min >= 45:
    print("Интересное время, которое я не смог распознать")
else:
    print("Вы ввели несуществующее время")









