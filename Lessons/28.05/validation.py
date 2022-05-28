while True:
    value = input("Please enter the time value if the format hh:mm\n")

    if len(value) != 5:
        print("The value has incorrect length, maybe you type something wrong")
        continue

    if value[2] != ':':
        print("You've missed the ':' symbol")
        continue

    values = value.split(':')
    hours, minutes = values[0], values[0]

    if not (hours.isdigit() and minutes.isdigit()):
        print("The hours and minutes must be digits")
        continue

    hours, minutes = int(hours), int(minutes)

    if hours > 24 or minutes > 60:
        print("The hours or minutes values is too big")
        continue

    break

print("the main logic goes here")