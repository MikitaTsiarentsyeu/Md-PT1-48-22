
string = 'The quicK Brown FoX'

# First variant

def check_str(string):
    string1 = string.replace(' ', '')
    string2 = (string.lower()).replace(' ', '')
    # print (string1)
    # print (string2)
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


# Second variant using ORD():

def check_str(string):
    string1 = string.replace(' ', '')
    string2 = (string.lower()).replace(' ', '')
    # print (string1)
    # print (string2)
    case_upper = []
    case_lower = []
    for i in range(len(string1)):
        if ord(string1[i]) == ord(string2[i]):
            case_lower.append(string2[i])
        else:
            case_upper.append(string2[i])
    print(len(case_lower))
    print(len(case_upper))

check_str(string)




