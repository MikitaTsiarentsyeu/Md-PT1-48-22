while True:
    str_len = input('Please enter your symbols charapter (from 35 to 50):\n')
    if not str_len.isdigit():
        print ('Error, your data type is not correct, please enter number')
        continue

    str_len = int(str_len)

    if str_len < 35 or str_len > 50:
        print ('Error, please enter number more from 35 to 50')
        continue
    break

with open("new_text.txt", 'w'): pass 
with open("text.txt", 'r') as f:
    lines = f.readlines()

n_lines = len(lines)

for i in range(n_lines):
    new_len = str_len 
    place = 0
    t_i = lines[i]

    while True:
        check = t_i[place: place + str_len + 1]   
        if check == '':
            break

        s = (check[::-1]) 
        new_len = str_len - s.find(' ')

        check = t_i[place : place + new_len] 
        place += new_len + 1
        add_space = str_len - new_len 
        first = check.split(' ')
        lenght_first = len(first)
        space_all = add_space // (lenght_first) 
        n_add_space = add_space % (lenght_first)
        for i in range(n_add_space):
            first[i] += " "
        space = " " * (space_all + 1)
        join_str = space.join(first) 

        with open("new_text.txt", 'a') as f:
            f.write(join_str + '\n')

print("New formated file was written as new_text.txt")