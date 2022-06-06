text_str = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"
numbers = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
         "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
         "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20}
numbers = list(set([numbers[i] for i in text_str.split()])) 
print(numbers)
numbers = [[numbers[i]*numbers[i+1], numbers[i+1] + numbers[i+2]] for i in range(0, len(numbers)-2, 2)] 
numbers = [item for sublist in numbers for item in sublist] 
print(numbers)
print(sum([i for i in numbers if i % 2 != 0])) 