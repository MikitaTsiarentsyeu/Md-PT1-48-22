from itertools import cycle


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
         open(f'Tasks/Kashko/task_03/justified_text_{limit}.txt', 'w') as wf:

        for line in rf:
            words = line.split()

            while words:
                buf = [words.pop(0)]

                while len(' '.join(buf)) < limit and words:
                    buf.append(words.pop(0))

                buf_len = len(' '.join(buf))

                if buf_len > limit:
                    words.insert(0, buf.pop())
                    buf_len -= len(words[0]) + 1
                    spaces = limit - buf_len

                    for i in cycle(range(len(buf) - 1)):
                        if spaces == 0:
                            break
                        buf[i] += ' '
                        spaces -= 1

                wf.write(' '.join(buf) + '\n')


print(justify_text(set_max_char_quantity()))
