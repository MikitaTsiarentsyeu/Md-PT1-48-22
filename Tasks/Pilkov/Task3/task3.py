from os import path as os_path


def get_number_of_characters_on_row_from_console():
    user_input = None

    while user_input is None:
        user_input = input('Type max number of character on row(from 35 to 50)\n')
        try:
            user_input = int(user_input)
        except ValueError:
            print('Plase enter integer on input field')
            user_input = None
        else:
            if user_input > 50 or user_input < 35:
                print('Number should be between 35 and 50')
                user_input = None

    return user_input

def create_new_char_formated_file(read_text_path, write_text_path, row_len):
    # errors='replace' was added because on my OS I always get
    # UnicodeDecodeError: 'utf-8' codec can't decode byte 0x9c in position 0: invalid start byte
    with open(f"{read_text_path}", 'r', errors='replace') as file:
        with open(f"{write_text_path}", 'w') as new_file:
            buffer = file.read(row_len + 1)
            
            while len(buffer) != 0:

                if '\n' in buffer:
                    buffer = buffer.split('\n')
                    last_word_len_counter = len(buffer[-1])
                    file.seek(file.tell() - last_word_len_counter)
                    buffer = ' '.join(buffer[:-1])
                elif buffer[-1] == ' ':
                    buffer = buffer[:-1]
                elif len(buffer) <= row_len:
                    pass
                else:
                    # save last word in file
                    splited_buffer = buffer.split()
                    last_word_len_counter = len(splited_buffer[-1])
                    file.seek(file.tell() - last_word_len_counter)
                    splited_buffer = splited_buffer[:-1]

                    # get places for spaces and total oter words lenght
                    spaces_counter = len(splited_buffer) - 1
                    char_sum_in_words = sum([len(word) for word in splited_buffer])

                    req_spaces = row_len - char_sum_in_words
                    avg_spaces = req_spaces // spaces_counter
                    req_spaces = req_spaces % spaces_counter

                    # add extra spaces for row banancing
                    for number, _ in enumerate(splited_buffer):
                        if number < req_spaces:
                            splited_buffer[number] = f'{splited_buffer[number]}{" "}'

                    buffer = f'{" "*avg_spaces}'.join(splited_buffer)
                
                new_file.write(f'{buffer}\n')
                
                buffer = file.read(row_len + 1)



if __name__ == '__main__':
    read_text_path = os_path.join(os_path.dirname(__file__), 'text.txt')
    write_text_path = os_path.join(os_path.dirname(__file__), 'new_text.txt')

    row_len = get_number_of_characters_on_row_from_console()

    create_new_char_formated_file(read_text_path, write_text_path, row_len)
    print(f'Formated file was created on location: {write_text_path}')