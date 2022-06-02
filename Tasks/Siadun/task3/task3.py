import random
while True:
    user_line = input ('Specify the desired dependency. The minimum number of characters is 35, the maximum is 50\n')
    if user_line.isdigit():
        if 51 > int(user_line) > 34:
            user_line = int(user_line)
            break
    print("invalid string length input.")
    
with open('text.txt', 'r', encoding='utf-8') as source_text:
    with open('text_task3.txt','w', encoding='utf-8') as changed_text:
        for f in source_text:
            line_new, len_line_new = [], 0
            line = f.split()
            for s  in line:
                if len(s) < (user_line - len_line_new):
                    line_new.append(s)
                    len_line_new += (len(s) + 1)
                    if len_line_new - 1 == user_line:
                        changed_text.write(' '.join(line_new)+'\n')
                        line_new, len_line_new = [], 0
                    elif len_line_new < user_line and s == line[len(line) - 1]:
                        changed_text.write(' '.join(line_new)+'\n')
                else:
                    while len_line_new < user_line:
                        line_new[random.randint(0, len(line_new)-2)] += (' ')
                        len_line_new += 1
                    changed_text.write(' '.join(line_new)+'\n')
                    line_new, len_line_new = [s], len(s) + 1            
        else:
            print("The modified text is written in new file 'changed_text'")            