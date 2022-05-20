# -*- coding: utf-8 -*-
import datetime
import re

hours_1 = {
    1: 'один час', 2: 'два часа', 3: 'три часа', 4: 'четыре часа',
    5: 'пять часов', 6: 'шесть часов', 7: 'семь часов', 8: 'восемь часов',
    9: 'девять часов', 10: 'десять часов', 11: 'одиннадцать часов', 12: "двенадцать часов", 0: "двенадцать часов"
}
hours_2 = {
    1: 'одна', 2: 'двe', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь',
    9: 'девять', 10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать',
    14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'
}
hours_3 = {
    59: 'одной', 58: 'двух', 57: 'трех', 56: 'четырех', 55: 'пяти', 54: 'шести', 53: 'семи',
    52: 'восьми', 51: 'девяти', 50: 'десяти', 49: 'одиннадцати', 48: 'двенадцати', 47: 'тринадцати',
    46: 'четырнадцати', 45: 'пятнадцати'
}
hours_4 = {1: 'десять', 2: 'двадцать', 3: 'тридцать', 4: 'сорок', 5: 'пятьдесят', 20: 'двадцать', 40: 'сорок'}
revHours = {
    12: 'первого', 1: 'второго', 2: 'третьего', 3: 'четвертого', 4: 'пятого', 5: 'шестого',
    6: 'седьмого', 7: 'восьмого', 8: 'девятого', 9: 'десятого', 10: 'одиннадцатого', 11: 'двенадцатого', 0: 'первого'
}
revHours2 = {1: 'два', 2: 'три', 3: 'четыре', 4: 'пять', 5: 'шесть',
             6: 'семь', 7: 'восемь', 8: 'девять', 9: 'десять',
             10: 'одиннадцать', 11: 'двенадцать', 12: 'первого', 0: 'час'}


class Time:
    """This class returns a string consist of 3 parts:
    1. Current time in accordance with minutes (0-min , 0<min<20, 20<min<30, 30-min, 30<min<45, 45<min<59)
    2. Word 'minutes' in appropriate case
    3. Hours in genitive case ( except min=00 and min>45 )
    """
    global hours_1, hours_2, revHours, hours_4, revHours2, hours_3

    def __init__(self, input_time):
        self.hour = input_time[0] % 12
        self.min = input_time[1]

    def makeResult(self):
        """return final result"""
        a, b, c = self.get_time(), self.get_minute(), self.get_hours()
        return f'{a} {b} {c}'

    def get_time(self):
        """return string for makeResult method"""
        if self.min == 0:
            return f'{hours_1[self.hour]} ровно'
        if 0 < self.min < 20:
            return f'{hours_2[self.min]}'
        if self.min == 30:
            return f'половина {revHours[self.hour]}'
        if 45 <= self.min < 60:
            return f'без {hours_3[self.min]}'
        if 20 < self.min < 45 and self.min not in (20, 40):
            return f'{hours_4[self.min // 10]} {hours_2[self.min % 10]}'
        if self.min in (20, 40):
            return f'{hours_4[self.min]}'
        return ''

    def get_minute(self):
        """this method returns formatted minutes for makeResult method"""
        if self.min % 10 in (2, 3, 4) and self.min not in [12, 13, 14, 52, 53, 54] or self.min == 59:
            return 'минуты'
        if self.min % 10 == 1 and self.min != 11:
            return 'минута'
        if self.min == 30 or self.min == 0:
            return ''
        return 'минут'

    def get_hours(self):
        """this method returns formatted hours for makeResult method"""
        if 0 < self.min < 45 and self.min != 30:
            return revHours[self.hour]
        if 45 <= self.min <= 59:
            return revHours2[self.hour]
        return ''


def convertTime(time):
    '''return list and separate by colon'''
    start = [int(i) for i in time.split(':')]
    return start

while True:
    user_choose = input('''Вам доступен следующий функционал:
    1. Вывод текущего времени: клавиша "1" 
    2. Завершение выполнения программы: клавиша '2'
    3. Ввод времени вручную в формате hh:mm: 
    -> ''')

    if user_choose == '1':
        time = datetime.datetime.now().strftime('%H:%M')
        n = Time(convertTime(time))
        result = f'Текущее время: {n.makeResult()}'
        print('#'*50)
        print(result)
        print('#'*50)
        continue
    if user_choose == '2':
        break

    if re.match('^([0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$', user_choose):
        converted = convertTime(user_choose)
        inp = Time(converted)
        print('#'*50)
        print(f'Введенное время: {user_choose} - {inp.makeResult()}')
        print('#'*50)
    else:
        print('#' * 50)
        print('Введите корректное время в формате hh:mm')
        print('#' * 50)
        
