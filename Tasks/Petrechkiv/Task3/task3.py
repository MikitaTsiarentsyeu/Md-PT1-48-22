while True:
    quantity = input('Enter the number of characters per line that is greater than 35 and less than 50: ')
    if not (quantity.isdigit()):
        print('Your input should contain only numbers. Try again')
        continue
    quantity = int(quantity) 
    if quantity < 35 or quantity > 50:
        print('Your value should be greater than 35 and less than 50. Try again')
        continue
    break  
position = 0
def words_counter(l):
    size = len(' '.join(l)) 
    return size 
with open('text.txt', 'r', encoding='utf-8') as text:
    with open('edited_text.txt', 'a', encoding='utf-8') as copy:
        while True:
            part = text.read(quantity+1)
            if part:
                if len(part) < quantity:
                    line = part.split()
                elif part[-1] != ' ':
                    line = part.split()
                    del line[-1]
                else:
                    part = part[:-1]
                    line = part.split() 
                position +=  len(' '.join(line).encode())+1
                if '\n' in part[:-1]:
                    position+=1
                if part[0] == ' ':
                    position+=1
                text.seek(position)
                if len(line) > 1:
                    while words_counter(line)<quantity:
                        for i in range(len(line)-1):
                            if words_counter(line)<quantity:
                                line[i]+=' '
                            else:
                                break
                new_line = ' '.join(line)
                copy.write(new_line + '\n')
            else: 
                break  
print('New file with the formatted text has been created.')                   