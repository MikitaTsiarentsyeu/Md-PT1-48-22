# binary search with recursion

def binary(list, item, low = None, high = None):
    if high is None and low is None:
        low = 0
        high = len(list)-1
    if low > high:
        return -1
    mid = (low + high)//2 
    if list[mid] == item:
        return mid
    elif list[mid] > item:
        return binary (list, item, low, mid-1)
    else:
        return binary (list, item, mid+1, high)
        
print(f'Index: {binary(list,5)}')

#------------------------------------------------------

# lambda x: int(x) == int

l = ['1', '11', '12', '22', '2', '13', '30', '33']

print(list(map(lambda x: str(int(x)**2) ,(sorted(filter(lambda x: int(x)%2 == 0, l), key = int)))))  