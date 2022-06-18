# 1. Реализовать функцию check_str которая получает на вход непустую строку и выдаёт информацию о количестве букв в верхнем и нижнем регистре.
# check_str('The quick Brown Fox') -> '3 upper case, 12 lower case'

string = 'The quicK Brown FoX'

def check_str(string):
    string1 = string.replace(' ', '')
    string2 = (string.lower()).replace(' ', '')

    case_upper = []
    case_lower = []
    
    for i in string1:
        if i in string2:
            case_lower.append(i)
        else:
            case_upper.append(i)
    print(len(case_lower))
    print(len(case_upper))

check_str(string)