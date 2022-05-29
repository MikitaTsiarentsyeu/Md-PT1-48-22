# data input by user
maxLength = int(input('Enter max number of symbols(from 35 to 50):\n'))

# work with files
if 7 < maxLength < 50:
    with open('text.txt', 'r', encoding= 'UTF8') as f:
        with open('newText.txt', 'w', encoding= 'UTF8') as copy:
            counter_2 = 0

# the way we format text            
            while True:
                subline = f.readline(maxLength+1)
                counter = 0
                if subline[-2] == ' ' or subline[-1] == ' ':
                    subline = subline[:maxLength].strip()
                    counter += 1
                else:
                    for i in subline[::-1]:
                        if i != ' ':
                           counter += 1
                        else:
                            break
                    subline = subline[:len(subline)-counter-1].strip()

# the way we add spaces:
                for i in range(len(subline)-1, -1, -1):
                    if len(subline) < maxLength and (subline[i] == ' ' and subline[i+1] != ' '):
                        subline = subline[:i+1] + ' ' + subline[i+1:]
                        print(subline)
                        print(len(subline))                  
                copy.write(subline + '\n')
                counter_2 += maxLength + 1 - counter
                f.seek(counter_2)

                if not subline:
                    break

                