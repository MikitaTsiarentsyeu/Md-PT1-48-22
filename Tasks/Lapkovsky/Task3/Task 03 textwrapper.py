while True:
    # entering a parameter
   length_str = input('Please, enter the length of the string, it must be more than 35 and less than 50 symbols:\n ')
   if length_str.isdigit():
        if int(length_str) > 35 and int(length_str) < 50 :
            length_str = int(length_str)
            break
        else:
            print("Check your value, please (35 - 50s)")
   else:
        print("Error! Enter a numeric value.")
    # reading the contents of the file and text formatting
with open('text.txt','r', encoding= 'utf8') as f:
    line = f.readlines()
with open('new_text.txt','w',encoding= 'utf8') as f:
    text = " "
    counter = 0
    for i in line:
        for j in i.split():
            new_count = counter+len(j)
            if counter !=0:
                new_count +=1
            if new_count >= length_str:
                text += "\n"
                counter = 0
            if counter !=0:
                text += ' '
                counter += 1
            text += j
            counter += len(j)
    txt_new = text.split('\n')
    for l in txt_new:
        checked = l.count(' ')
        if len(l) < length_str and checked !=0:
            final = (length_str-len(l))//checked
            surplus = (length_str-len(l))%checked
            if final > 0:
                l=l.replace(' ',(' ') + (' ') *final)
            if surplus > 0:
                l=l.replace((' ') + (' ') *final,(' ') + (' ')*final + (' '),surplus)
        l = l + '\n'
        f.writelines(l)
print('Your file is ready, check > ''new_text.txt')