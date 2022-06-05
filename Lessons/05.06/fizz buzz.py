# for i in range(1, 101): 
#     print("Fizz"*(i%3==0)+"Buzz"*(i%5==0) or str(i))

# for i in range(1, 101): 
#     res = ""
#     if i%3==0:
#         res+="fizz"
#     if i%5==0:
#         res+="buzz"
#     print(res or i)

fizz = "Fizz"
buzz = "Buzz"
first_num = 3
second_num = 5
low = 1
high = 101

def check_rem(i, x):
    return i%x == 0

def mult_token(token, num):
    return token*num

def main():
    print([mult_token(fizz,check_rem(i, first_num))+mult_token(buzz, check_rem(i, second_num)) or i for i in range(low, high)])

# print([fizz*(i%first_num==0)+"Buzz"*(i%second_num==0) or i for i in range(low, high)])