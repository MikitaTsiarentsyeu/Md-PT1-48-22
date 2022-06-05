d = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
     "eleven": 11, "twelfth": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
     "eighteen": 18, "nineteen": 19, "twenty": 20}

data = list(set([d[i] for i in input().split()]))

print(*[f"Multiplying the {i+1} and {i+2} number in list = {data[i] * data[i + 1]}" if i % 2 == 0 else f"Addition the {i+1} and {i+2} number in list = {data[i] + data[i + 1]}" for i in range(len(data) - 1)], sep="\n")

print(f"Sum of all odd numbers: {sum([i for i in data if i % 2 != 0])}")
