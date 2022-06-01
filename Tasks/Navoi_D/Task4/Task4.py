text_str = "five fifteen two eleven seventeen two one thirteen ten four eight five nineteen"
res = {"zero": "0", 
         "one": "1", 
         "two": "2",
         "three": "3", 
         "four": "4", 
         "five": "5",
         "six": "6",
         "seven":"7",
         "eight":"8",
         "nine": "9",
         "ten": "10",
         "eleven": "11",
         "twelve": "12",
         "thirteen": "13",
         "fourteen": "14",
         "fifteen": "15",
         "sixteen": "16",
         "seventeen": "17",
         "eighteen": "18",
         "nineteen": "19",
         "twenty": "20"}
#convert to numbers
res =list(set([res[i] for i in text_str.split()])) 

#delete duplicates and sorting ascending
res = sorted([int(digit) for digit in res]) 

#input in the list the multiplication of the 1st and 2nd, the sum of the 2nd and 3rd, etc.
res = [[res[i]*res[i+1], res[i+1] + res[i+2]] for i in range(0, len(res)-2, 2)] 
res = [item for sublist in res for item in sublist] # take sublist out of the list
print(res)

# determine even numbers, display the sum of the numbers in the list
print(sum([i for i in res if int(i) % 2 == 0])) 

