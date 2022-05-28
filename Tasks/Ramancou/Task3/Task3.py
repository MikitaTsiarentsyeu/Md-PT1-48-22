import os

class Solution:
    def text_justify(self, words, wrap):
        """
        :type words: gets a list of strings
        :type wrap: gets int parameter of string width
        :return: list with given width
        """
        current_line = []
        current_width = 0
        result = []

        for word in words:
            if current_width + len(current_line) + len(word) > wrap:
                spaces_count = len(current_line) - 1 if len(current_line) - 1 else 1
                for i in range(wrap - current_width):
                    current_line[i % spaces_count] += ' '
                result.append(''.join(current_line))
                current_width = 0
                current_line = []
            current_width += len(word)
            current_line.append(word)
        last_line = ' '.join(current_line).strip()
        result.append(last_line := last_line + " " * (wrap - len(last_line)))
        return result

def recording(name,wrap):
    with open(os.path.realpath(r'..\..\!Tasks\Task3\text.txt'), 'r',  encoding='utf-8') as f:
        with open(f'{name}.txt', 'w', encoding='utf-8') as r:
            long_string_list = ''.join(f.readlines()).split('\n')
            one_string = ' '.join(long_string_list).split()
            r.write('\n'.join(x := Solution().text_justify(one_string, wrap)))


if __name__ == '__main__':
    while True:
        try:
            user_input = input('Enter the column width (from 35 to 50): ')
            len_check = True if user_input.isdigit() and 35 <= int(user_input) <= 50 else False
            if len_check:
                user_name = input('Enter new file name (ex:"result"): ')
                recording(user_name, int(user_input))
                print(f'You successfully recorded {user_name}.txt file')
                break
            else: print('Please, enter number in range from 35 to 50')
        except FileNotFoundError:
            print('Check a path of main File or Directory')
            break
