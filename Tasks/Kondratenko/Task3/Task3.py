import os

while True:
    text_width = input("Please enter maximum number of characters per line (from 35 to 50):\n")
    if text_width.isdigit():
        text_width = int(text_width)
    else:
        print("Input must contain only numbers!")
        continue
    if 35 <= text_width <= 50:
        break
    else:
        print("Enter numbers from 35 to 50!")
        continue

out_length = 0
end_file_flag = False

try:
    with open("text.txt", encoding="utf-8") as source:
        with open("align.txt", "w", encoding="utf-8") as align:
            while True:
                line = source.read(text_width + 1 - out_length)
                if line == "":
                    break
                if len(line) < text_width + 1 - out_length:
                    end_file_flag = True
                out_length = 0
                if "\n" in line:
                    n_index = line.find("\n")
                    align.write(line[:n_index + 1] + "\n" + line[n_index + 1:])
                    out_length = len(line[n_index + 1:])
                elif line[-1] == " ":
                    align.write(line[:len(line) - 1] + "\n")
                elif line[-1] != " " and not end_file_flag:
                    space_index = line.rfind(" ")
                    align.write(line[:space_index] + "\n" + line[space_index + 1:])
                    out_length = len(line[space_index + 1:])
                elif end_file_flag:
                    align.write(line)
except:
    print("Left alignment error")

try:  # add spaces in align.txt
    with open("align.txt", "r+", encoding="utf-8") as align:
        lst = align.readlines()
        for i in range(len(lst)):
            while len(lst[i][:-1]) < text_width:
                if i == len(lst) - 1:
                    break
                elif lst[i + 1] == "\n":
                    break
                elif lst[i] == "\n":
                    break
                required = text_width - len(lst[i][:-1])
                lst[i] = lst[i].replace(" ", "  ", required)
        while "\n" in lst:
            lst.remove("\n")
        align.seek(0)
        align.writelines(lst)
except:
    print("File read error ")
finally:
    print(f"Width alignment done\nSee file align.txt in {os.getcwd()}")
