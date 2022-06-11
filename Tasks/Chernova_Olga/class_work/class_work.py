from text_to_num import text2num

num = ("five thirteen two eleven seventeen two one thirteen ten four eight five nineteen").split()

for i in range(len(num)):
    num[i] = text2num(num[i],'en')

num = list(set(num))
  
for i in range(len(num)-1):
    print(f'The product of {i+1} and {i+2} numbers: {num[i] * num[i+1]}') if i % 2 == 0 else print(f'The sum of {i+1} and {i+2} numbers: {num[i] + num[i+1]}')

print(f'\nThe total sum of odd numbers: {sum(i for i in num if i % 2 != 0)}')
