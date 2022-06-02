# import cProfile
from itertools import cycle

# from random import randint


def set_max_char_quantity() -> int:
    """Reads user input and returns characters limit for one line.

    Input format: integer.

    Returns:
        int: integer.
    """

    while True:

        try:
            max_chars = input(
                'Enter characters limit in range from 35 to 50:\n')
            max_chars = int(max_chars)
            if any((max_chars < 35, max_chars > 50)):
                raise ValueError('Characters limit must be between 35 and 50')
            return max_chars
            break

        except ValueError as error:
            print(f'Invalid number: {error}.')


def justify_text(limit: int) -> None:
    """Creates file's copy and writes justified text to it.

    Args:
        limit (int): characters limit per line.
    """

    with open('Tasks/!Tasks/Task3/text.txt', 'r') as rf, \
         open(f'Tasks/Kashko/task_03/results/'
              f'justified_text_{limit}.txt', 'w') as wf:

        for line in rf:
            words = line.split()

            while len(' '.join(words)) > limit:
                buffer = [words.pop(0)]
                buffer_length = len(' '.join(buffer))

                while buffer_length < limit:
                    next_word_length = len(words[0])
                    if buffer_length + next_word_length + 1 > limit:
                        break
                    buffer.append(words.pop(0))
                    buffer_length += next_word_length + 1

                spaces = limit - buffer_length

                for i in cycle(range(len(buffer) - 1)):
                    if spaces == 0:
                        break
                    buffer[i] += ' '
                    spaces -= 1

                wf.write(' '.join(buffer) + '\n')

            wf.write(' '.join(words) + '\n')


# with cProfile.Profile() as pr:
#     for _ in range(10000):
#         justify_text(randint(35, 50))

# pr.print_stats()

if __name__ == '__main__':
    try:
        justify_text(set_max_char_quantity())
    except FileNotFoundError as error:
        print(f'Error occurred: {error}')
    finally:
        print('Program finished.')
