from math import sqrt


def check_str(text, language="en"):
    """ Function count upper and lower case in input text.
    Text must be written in English or Russian"""

    upper_case = {"ru": [1040, 1071], "en": [65, 90]}
    lower_case = {"ru": [1072, 1103], "en": [97, 122]}
    try:
        text = text.encode().decode("utf-8")
        upper_case_characters = lower_case_characters = 0
        for i in text:
            if ord(i) == 32:
                continue
            elif upper_case[language][0] <= ord(i) <= upper_case[language][1]:
                upper_case_characters += 1
            elif lower_case[language][0] <= ord(i) <= lower_case[language][1]:
                lower_case_characters += 1
        return f"{upper_case_characters} upper case, {lower_case_characters} lower case"
    except:
        return "file encoding error"


def is_prime(number):
    """Function determines if the input number is prime"""

    if number == 1:
        print(False)
        return

    i = 2
    flag = True
    while i <= sqrt(number):
        if number % i == 0:
            flag = False
            break
        i += 1
    print(flag)


def get_ranges(lst):
    """The function converts the list to a rolled form"""

    rolled_list = []
    flag = False

    for i in range(len(lst) - 1):
        if lst[i] + 1 == lst[i + 1]:
            if not flag:
                first_number = lst[i]
                flag = True
            else:
                continue
        else:
            if not flag:
                rolled_list.append(str(lst[i]))
            else:
                rolled_list.append(f"{str(first_number)}-{str(lst[i])}")
                flag = False

        if i == len(lst) - 2:  # crutch for the last value in the list
            if not flag:
                rolled_list.append(str(lst[i + 1]))
            else:
                rolled_list.append(f"{str(first_number)}-{str(lst[i + 1])}")

    print(", ".join(rolled_list))


# Call 1 function
print(check_str(input("Enter text:\n"), input("Enter language (en or ru):\n")))
# Call 2 function
is_prime(777)
# Call 3 function
get_ranges([0, 1, 2, 3, 4, 7, 8, 10])
get_ranges([4, 7, 10])
get_ranges([2, 3, 8, 9])
