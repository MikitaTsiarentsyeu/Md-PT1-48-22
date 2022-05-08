years = 5
money = 20000
percent = 15
capitalization = "monthly" # We can have 'quarterly', 'monthly' or 'daily'

new_sum = money

##It's my program. I didn't look in the internet

#if (years, money,percent) is int or float:
#    for i in range(0,years*12):
#        new_sum +=  new_sum*percent/12/100
#    print("You will have in the bank", round(new_sum,4), ' the interest on the deposit will be ', round((new_sum-money),4))
#else:
#    print('You have errors in the data ')




#It's program when i was look in the intenet
if ((years, money,percent) is int or float) and (capitalization == 'daily' or capitalization == 'monthly' or capitalization == 'quarterly'):
    if capitalization == 'quarterly':
        new_sum = new_sum * (1+percent/100/4)**(years*4)
        print("You will have in the bank", round(new_sum,4), ' the interest on the deposit will be ', round((new_sum-money),4))
    elif capitalization == 'monthly':
        new_sum = new_sum * (1+percent/100/12)**(years*12)
        print("You will have in the bank", round(new_sum,4), ' the interest on the deposit will be ', round((new_sum-money),4))
    else:
        begin_year = int(input('In what year will the deposit be opened? '))  
        for i in range(begin_year, begin_year + years):
            if (i % 400 == 0) or (i % 4 ==0 and i % 100 != 0):
                new_sum = new_sum * (1+percent/100/366)**366           
            else:
                new_sum = new_sum * (1+percent/100/365)**365
        print("You will have in the bank", round(new_sum,4), ' the interest on the deposit will be ', round((new_sum-money),4))
else:
    print('You have errors in the data ')