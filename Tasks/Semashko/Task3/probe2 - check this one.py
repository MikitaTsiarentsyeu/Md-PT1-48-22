#  Enter max number od symbols per line and validation
while True:  
   maxLength = input('Enter max number of symbols(from 35 to 50):\n')
   if maxLength.isdigit():
        if 35 < int(maxLength) < 50 :
            maxLength = int(maxLength)
            break
        else:
            print('!!!Enter a valid number!!!')
   else:
        print("Try again, please!")
# Open => Read => Format
with open('text.txt','r', encoding= 'UTF-8') as f:
    line = f.readlines()
with open('newText.txt','w', encoding= 'UTF-8') as copy:
    newText = ''
    counter = 0
    for i in line:
        for k in i.split():
            counter2 = counter + len(k)
            if counter != 0:
                counter2 += 1
            if counter2 >= maxLength:
                newText += "\n"
                counter = 0
            if counter != 0:
                newText += ' '
                counter += 1
            newText += k
            counter += len(k)
    newLine = newText.split('\n')
# add spaces
    for s in newLine:
        space_counter = s.count(' ')
        if len(s) < maxLength and space_counter != 0:
            x = (maxLength-len(s)) // space_counter
            y = (maxLength-len(s)) % space_counter
            if x > 0:
                s=s.replace(' ',(' ') + (' ') *x)
            if y > 0:
                s=s.replace((' ') + (' ') *x,(' ') + (' ')*x + (' '),y)
        print(s)
        s = s + '\n'
        
        copy.writelines(s)
print('A Text was copied to a new file and formated according to the max number of symbols.')
