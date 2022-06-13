

while True:
    symbols_number = input('Please enter your symbols charapter (from 35 to 50):\n')
    if not symbols_number.isdigit():
        print('Error, your data type is not correct, please enter number')
        continue
    symbols_number = int(symbols_number)
    if symbols_number < 35 or symbols_number > 50:
        print('Error, please enter number more from 35 to 50')
        continue
    break

with open("text.txt", 'r', encoding="utf-8") as f:
    with open("new_text.txt", 'w', encoding="utf-8") as write:

        for line in f:
            list_text = line.split()

            while len(' '.join(list_text)) > symbols_number:
                word = [list_text.pop(0)]
                len_words = len(' '.join(word))

                while len_words < symbols_number:
                    next_word_length = len(list_text[0])
                    if len_words + next_word_length + 1 > symbols_number:
                        break
                    word.append(list_text.pop(0))
                    len_words += next_word_length + 1

                space = symbols_number - len_words

                while space != 0:
                    for i in range(len(word) - 1):
                        if space == 0:
                            break
                        word[i] += ' '
                        space -= 1

                write.write(' '.join(word) + '\n')

            write.write(' '.join(list_text) + '\n')

