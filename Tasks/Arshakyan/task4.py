text = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"
number = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", 
"seven":"7", "eight":"8", "nine": "9", "ten": "10", "eleven": "11", "twelve": "12", "thirteen": "13",
"fourteen": "14", "fifteen": "15", "sixteen": "16", "seventeen": "17", "eighteen": "18",
"nineteen": "19", "twenty": "20"}

number = list(set([number[i] for i in text.split()])) 
print(number)

number = sorted([int(digit) for digit in number]) 
print(number)

number = [[number[i]*number[i+1], number[i+1] + number[i+2]] for i in range(0, len(number)-2, 2)] 
number = [item for sublist in number for item in sublist]
print(number)

print(sum([i for i in number if int(i) % 2 != 0])) 