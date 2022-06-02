# Finding the path to the file was very difficult for me in this task.
# I don't now it's my decision true or false.
# I decided to leave the program as it definitely worked.
# I would use the os module like this:
# 
# import os
# way = os.getcwd() + os.sep
# 
# And I would use the resulting way for all text files.
# For exemple:
# 
# with open(way + 'text.txt', 'a', encoding='utf-8') as f:
#     or
# new_f = open(way + 'new_text.txt', 'w', encoding='utf-8')


while True:
    length = input('What lenght should be for the string (min 35, max 50): ')

    if (length.isnumeric() is False):
        print('Your code contains invalid characters!')
        continue

    if (int(length) < 35) or (int(length) > 50):
        print("You're out of range")
        continue
    break

def app(text):
    '''Add a line to new file'''
    with open('new_text.txt', 'a', encoding='utf-8') as new_f:
        new_f.write(text + '\n')

length = int(length)

new_f = open('new_text.txt', 'w', encoding='utf-8')

with open("text.txt", 'a', encoding='utf-8') as f:
    f.write('\n')

with open("text.txt", "r", encoding='utf-8') as f:
    line = f.readline()
    while line != '':
        i = 0
        while i < len(line):
            string = line[i:length+i+1]

            if string.find('\n') != -1:
                app(string[:-1])
                i += length

            else:
                if string[0] == ' ':
                    string = string[1:]
                for j in range(len(string)-1, 0, -1):
                    if string[j] == ' ':
                        string = string[:j]
                        break

                num_space = length - len(string)
                string = string.split(' ')
                free_space = num_space % (len(string) - 1)
                    
                for k in range(len(string) - 1):
                    if free_space > 0:
                        string[k] = string[k] + ' '*(1 + (num_space // (len(string) - 1)) + 1)
                        free_space = free_space-1
                    else:
                        string[k] = string[k] + ' '*(1 + (num_space // (len(string) - 1)))

                string = ''.join(string)
                app(string)
                i += j + 1

        line = f.readline()
    else:
        print('New text is ready!')
