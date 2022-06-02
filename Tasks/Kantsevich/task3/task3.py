with open ('text.txt', 'r') as text:
    with open ('text-copy.txt', 'w') as copy:
        number = int(input('enter the number of characters for 1 line: '))
        text_lines = text.readlines()
        for x in text_lines:
            x = x.replace('\n', '')
            words =  x.split(' ')
            print(words, len(x))
            new_text = []
            k = 0
            for y in words:

                if k + len (y)+1 <= number:
                    new_text.append(y)
                    if k == 0:
                        k+=len(y)
                    else:
                        k += len(y)+1
                else:
                    number_of_space = number - k
                    h = 0
                    while number_of_space>0:
                        if len(new_text) == 1:
                            break
                        if len(new_text)==h+1:
                            h = 0
                            continue
                        new_text[h] = new_text[h] + ' '
                        number_of_space = number_of_space - 1
                        h+=1

                    new_text_with_space = ' '.join(new_text) +'\n'
                    new_text.clear()
                    k = len(y)
                    new_text.append(y)
                    copy.writelines(new_text_with_space)
            new_text_with_space = ' '.join(new_text)+'\n'
            copy.writelines(new_text_with_space)

