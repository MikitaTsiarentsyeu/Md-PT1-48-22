# Text copying and formating program

maxLength = int(input('Enter max number of symbols(from 35 to 50):\n'))

if 35 < maxLength < 50:
    with open('text.txt', 'r') as f:
        with open('newText.txt', 'w') as copy:
            subLine = f.read(maxLength+1)
            count = 0
            while subLine:
                f.seek(count * maxLength)
                if (subLine[-1] == ' ' and subLine[-2] != ' ') or (subLine[-1] != ' ' and subLine[-2] == ' '):
                    subLine = f.read(maxLength)
                    #print(subLine)          # просто посмотреть
                    #print(subLine[-1])  # просто посмотреть
                    subLine = subLine.strip()
                    print(subLine)      # просто посмотреть
                    #spaceNumb = maxLength - len(subLine)
                    #print(len(subLine))      # просто посмотреть
                    #print(spaceNumb)    # просто посмотреть
                    #print(subLine)   # просто посмотреть

                elif subLine[-1] != ' ' and subLine[-2] != ' ':
                    subLine = f.read(maxLength)
                    print(subLine)          # просто посмотреть
                    print(subLine[-1])  # просто посмотреть
                    subLine = subLine.strip()
                    listing = subLine.split()
                    transfer = listing[-1]
                    #listing.pop(-1)
                    #trans[i] = transfer
                    #print(listing)   # просто посмотреть
                    subLine = (' ').join(listing)
                    spaceNumb = maxLength - len(subLine)
                    #print(len(subLine))      # просто посмотреть
                    #print(spaceNumb)    # просто посмотреть
                   # print(subLine)   # просто посмотреть
                for i in range(len(subLine)-1, -1, -1):
                    if len(subLine) < maxLength and (subLine[i] == ' ' and subLine[i+1] != ' '):
                        subLine = subLine[:i+1] + ' ' + subLine[i+1:]
                        print(subLine)
                        print(len(subLine))
                copy.write(subLine + '\n')
                subLine = f.read(maxLength)
                count += 1

                
                      
        print('A Text was copied to a new file and formated according to the max number of symbols.')                
else:
    print('!!!Enter a valid number!!!')

#------------------------------------------------------------------------------------------------------
'''
with open('text.txt', 'r') as f:
    with open('newText.txt', 'w') as copy:
        subLine = f.read(maxLength+1)
        print(subLine)
        print(len(subLine))
        print(subLine[-1])
        if (subLine[-1] == ' ' and subLine[-2] != ' ') or (subLine[-1] != ' ' and subLine[-2] == ' '):
            f.seek(0)
            subLine = f.read(maxLength)
            print(subLine)          # просто посмотреть
            print(subLine[-1])  # просто посмотреть
            subLine = subLine.strip()
            print(subLine)
            spaceNumb = maxLength - len(subLine)
            print(len(subLine))      # просто посмотреть
            print(spaceNumb)    # просто посмотреть
            print(subLine)   # просто посмотреть
        elif subLine[-1] != ' ' and subLine[-2] != ' ':
            f.seek(0)
            subLine = f.read(maxLength)
            print(subLine)          # просто посмотреть
            print(subLine[-1])  # просто посмотреть
            subLine = subLine.strip()
            listing = subLine.split()
            transfer = listing[-1]
            print(f'trasfer element: {transfer}') # просто посмотреть
            listing.pop(-1)
            print(listing)   # просто посмотреть
            trans[0] = transfer
            subLine =(' ').join(listing)
            spaceNumb = maxLength - len(subLine)
            print(len(subLine))      # просто посмотреть
            print(spaceNumb)    # просто посмотреть
            print(subLine)   # просто посмотреть
        for i in range(len(subLine)-1, -1, -1):
            if len(subLine) < maxLength and (subLine[i] == ' ' and subLine[i+1] != ' '):
                subLine = subLine[:i+1] + ' ' + subLine[i+1:]
                print(subLine)          # просто посмотреть
                print(len(subLine))     # просто посмотреть
        copy.write(subLine + '\n')
        subLine = f.read(maxLength) 
'''         
