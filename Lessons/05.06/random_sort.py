import random

l = [3,5,1,7,2,8,9,6,4]

def generate_index(n):
    return random.randint(0, n-1)

def swap_items(l):
    n = len(l)
    i = generate_index(n)
    j = i
    while i == j:
        j = generate_index(n)
    l[i], l[j] = l[j], l[i]

def is_sorted(l):
    # return l == sorted(l)
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True

def sort_by_random(l):
    counter = 0
    while not is_sorted(l):
        swap_items(l)
        counter += 1

    print(counter)

sort_by_random(l)