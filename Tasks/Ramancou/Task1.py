def checkingInput(x):
    """Checking if the input value is a number and greater than zero """
    try:
        x = float(x)
        return True if x > 0 else False
    except:
        return False

def makeResult(startsum, years, procent):
    """Function responsible for calculation"""
    mounts = years * 12
    result = startsum * (((procent/100/12)+1) ** mounts)
    return round(result, 2)

#
templates = [
    'Deposit amount: ',
    'Deposit period (minimum 1 year): ',
    'Annual percentage rate: '
]

valuesList = []  # creating new list with correct user input
for templateLine in templates:
    userInput = input(templateLine)
    while True:   # endless loop until the user enters the correct data
        if checkingInput(userInput):
            valuesList.append(float(userInput))
            break
        else:
            print("Error! Please input correct value")
            userInput = input(templateLine)


print(f'''Your account balance in {int(valuesList[1])} years will be {makeResult(*valuesList)} BYN
Your profit will be  {round(makeResult(*valuesList)-valuesList[0],2)} BYN''')