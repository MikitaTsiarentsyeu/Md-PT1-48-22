max_characters = input("enter the maximum number of characters per line from 35 to 50\n")
max_characters = int(max_characters)
if 35 < max_characters < 50:
        print(max_characters)   
else:
    print("wrong input")

with open('Tasks/Papovich/Md-PT1-48-22/Tasks/!Tasks/Task3/text.txt', 'r',) as f:
    line = f.readlines() 
with open('new_text.txt','w') as f:
    text = " "
    counter=0
    for i in line:
        for j in i.split():
            new_count= counter+len(j)
            if counter !=0:
                new_count +=1
            if new_count >= max_characters:
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
        if len(l)<max_characters and probed !=0:
            total=(max_characters-len(l))//probed
            remainder=(max_characters-len(l))%probed
            if total > 0:
                l=l.replace(' ',(' ')+(' ')*total)
            if remainder > 0:
                l=l.replace((' ')+(' ')*total,(' ')+(' ')*total+(' '),remainder)
        l=l +'\n'
        f.writelines(l)
print('your document is ready in a new file ''new_text.txt')