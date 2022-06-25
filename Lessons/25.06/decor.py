def do_twice(func):
    def wrapper(*n):
        func(n[0], n[1])
        func(n[0], n[1])
    return wrapper

def comment_process(func):
    def wrapper(n, m):
        print("the process will be started")
        func(n, m)
        print("the process was finished")
    return wrapper

@do_twice
@comment_process
def print_numbers(n, m):
    print(n, m)

# print_number_four = do_twice(print_number_four)
# print_number_four = comment_process(print_number_four)

print_numbers(4,6,7,8,9,0)