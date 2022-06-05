try:
    l = [1,2,3,4,5]
    if len(l) > 3:
        raise MemoryError("the list is too big")
    # l[5]
    print("try logic goes on")
    try:
        l[5]
    except NameError:
        print("inner name error")
except IndexError as e:
    try:
        print(e)
        print(not_defined_name)
    except:
        print("how did it come to this?")
except (MemoryError, NameError) as e:
    print(e)
except:
    print("Something went really wrong")
finally:
    print("something that will be executed every time")

print("the logis goes on")

# with open("test.txt") as f:
#     f.write("test")

# the same as

# try:
#     f = open("test.txt")
#     f.write("test")
# finally:
#     f.close()