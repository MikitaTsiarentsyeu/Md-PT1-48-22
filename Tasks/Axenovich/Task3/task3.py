import os

while True:
    user_input = input("Please input maximum number of characters in a string (from 35 to 50)\n")

    if user_input.isdigit():
        if 51 > int(user_input) > 34:
            user_input = int(user_input)
            break
    print("Incorrect input, please try again.\n")

def write_join_text(out, line_out):
    out.write(' '.join(line_out)+'\n')

with open(os.path.join(os.getcwd(), "Tasks", "!Tasks", "Task3", "text.txt"), 'r', encoding='utf-8') as text:
    with open(os.path.join(os.getcwd(), "Tasks", "Axenovich", "Task3", "formatted_file.txt"), 'w', encoding='utf-8') as copy:
        for i in text:
            line_out, len_line_out = [], 0
            line = i.split()
            for j in line:
                if len(j) <= (user_input - len_line_out):
                    line_out.append(j)
                    len_line_out += (len(j) + 1)
                    if len_line_out - 1 == user_input:
                        write_join_text(copy, line_out)
                        line_out, len_line_out = [], 0
                    elif len_line_out < user_input and j == line[len(line) - 1]:
                        write_join_text(copy, line_out)
                else:
                    len_spaces = user_input - (len_line_out - 1)
                    a, b = len_spaces // (len(line_out) - 1), len_spaces % (len(line_out) - 1)
                    for k in range(len(line_out) - 1):
                        line_out[k] += (' ' * a)
                    for k in range(b):
                        line_out[k] += ' '
                    write_join_text(copy, line_out)
                    line_out, len_line_out = [j], len(j) + 1
        else:
            print("\nDear user! The text is written to a new file 'text_new.txt' ")
