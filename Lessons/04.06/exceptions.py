try:
    l = []
    l[0] = 1
    print(l[0])
except NameError as e:
    print(e)
except IndexError as e:
    print(e)
except:
    print("oh noes!")

print("the end")