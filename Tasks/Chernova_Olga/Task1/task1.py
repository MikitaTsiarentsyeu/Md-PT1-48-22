years = input('For how long do you want to make a deposit? ')
money = input('How much do you want to deposit? ')
percent = input('What is the percentage of the deposit? ')
capitalization = input(' Capitalization is: (quarterly is q, monthly is m, daily is d) ')

new_sum = money

##It's my program. I didn't look in the internet

if years.isnumeric() and money.isnumeric() and percent.isnumeric():
    years = int(years)
    money = int(money)
    percent = int(percent)
    if years > 0 and money > 0 and percent > 0:   
       for i in range(0,years*12):
           new_sum +=  new_sum*percent/12/100
       print(f"You will have in the bank {round(new_sum,4)} the interest on the deposit will be {round((new_sum-money),4)}")
    else:
        print('You have errors in the data ')
else:
    print('You have errors in the data ')




#It's program when i was look in the intenet

def leap_year(year):
    if year % 400 ==0 or (year % 4 ==0 and year % 100 != 0):
        extra_day = 1
    else:
        extra_day = 0
    return extra_day

if (years.isnumeric() and money.isnumeric() and percent.isnumeric()) and (capitalization == 'd' or capitalization == 'm' or capitalization == 'q'):
    years = int(years)
    money = int(money)
    percent = int(percent)
    if years > 0 and money > 0 and percent > 0:
        if capitalization == 'q':
            new_sum = new_sum * (1+percent/100/4)**(years*4)
            print(f"You will have in the bank {round(new_sum,4)} the interest on the deposit will be {round((new_sum-money),4)}")
        elif capitalization == 'm':
            new_sum = new_sum * (1+percent/100/12)**(years*12)
            print(f"You will have in the bank {round(new_sum,4)} the interest on the deposit will be {round((new_sum-money),4)}")
        else:
            begin_year = input('In what year will the deposit be opened? ') 
            if begin_year.isnumeric():
                begin_year = int(begin_year)
                days = 0
                for i in range(begin_year, begin_year + years):
                    days = 365 + leap_year(i)
                    new_sum = new_sum * (1+percent/100/days)**days
                print(f"You will have in the bank {round(new_sum,4)} the interest on the deposit will be {round((new_sum-money),4)}")
            else:
                print('You have errors in the year ')
    else:
        print('You have errors in the data ')
else:
    print('You have errors in the data ')