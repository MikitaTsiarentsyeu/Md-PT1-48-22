import time_decor

@time_decor.time_measure
def counter(n=100):
    # raise ArgumentError
    r = 0
    for i in range(1, n+1):
        r+=i
    return r

try:
    print(counter(100000))
    print(time_decor.get_time_res())
except:
    print("Oooops")

    