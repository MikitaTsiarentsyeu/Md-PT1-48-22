while True:
   string_len = input('enter the length of the string, it must be greater than 35 and less than 50:\n ')
   if string_len.isdigit():
        if int(string_len) > 35 and int(string_len) < 50 :
            string_len = int(string_len)
            break
        else:
            print("Value must be over 35 and less than 50! Try again!")
   else:
        print("Input Error!!Please, enter a numeric value!")

with open('text.txt','r', encoding= 'utf8') as f:
    line = f.readlines()
with open('new_text.txt','w',encoding= 'utf8') as f:
    text = " "
    counter=0
    for i in line:
        for j in i.split():
            new_count= counter+len(j)
            if counter !=0:
                new_count +=1
            if new_count >= string_len:
                text += "\n"
                counter = 0
            if counter !=0:
                text += ' '
                counter += 1
            text += j
            counter += len(j)
    txt = text.split('\n')
    for l in txt:
        probed = l.count(' ')
        if len(l)<string_len and probed !=0:
            total=(string_len-len(l))//probed
            remainder=(string_len-len(l))%probed
            if total > 0:
                l=l.replace(' ',(' ')+(' ')*total)
            if remainder > 0:
                l=l.replace((' ')+(' ')*total,(' ')+(' ')*total+(' '),remainder)
        l=l +'\n'
        f.writelines(l)
print('your document is ready in a new file ''new_text.txt')



