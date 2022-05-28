with open("text.txt", "r") as f:
    string = f.read()

while True:
    line_width = input("Enter the maximum number of symbols in the line (from 36 to 50):\n")
    if not line_width.isdigit():
        print("Number of symbols must be digits.\n")
        continue
    if int(line_width) > 50 or int(line_width) < 36:
        print("Enter the number of symbols in the line from 36 to 50.\n")
        continue
    break
line_width = int(line_width)
def split_spaces(string, line_width):
    lower_bound = 0
    upper_bound = 0
    last_space = string.rindex(' ')
    while upper_bound < len(string):
        upper_bound = string.rindex(' ', lower_bound, lower_bound + line_width)
        if upper_bound == last_space:
            upper_bound = len(string)
        yield string[lower_bound:upper_bound].strip()
        lower_bound = upper_bound

formatted_text = "\n".join(split_spaces(string, line_width)).split("\n")
with open("text_2.txt", "w") as copy:
    for i in formatted_text:
        spaces = i.count(' ')
        if len(i)<line_width and spaces != 0:
            k1=(line_width-len(i))//spaces
            k2=(line_width-len(i))%spaces
            if k1 > 0:
                i=i.replace(' ',(' ')+(' ')*k1)
            if k2 > 0:
                i=i.replace((' ')+(' ')*k1,(' ')+(' ')*k1+(' '),k2)
            i=i +'\n'
            copy.write(i)
        



