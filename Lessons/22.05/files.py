# f = open("test.txt", 'w')
# print(f)
# f.write("test line number 1")
# f.close()

with open("test.txt", 'w') as f:
    f.write("test line number 1\n")
    f.write("test line number 2\n")
    f.writelines(["test line number 3\n", "test line number 4\n"])

with open("test.txt", 'r') as f:
    for s in f:
        print(s)
    # for s in f.readlines():
    #     print(s)
    # print(f.readline())
    # print(f.readline())
    # print(f.readline())
    # print(f.readlines())
    # print(f.read(10))
    # print(f.read())
    # f.seek(0)
    # print(f.read(10))
    
buffer = 10
with open("test.txt", 'r') as f:
    with open("test-Copy.txt", 'w') as copy:
        s = f.read(buffer)
        while s:
            copy.write(s)
            s = f.read(buffer)
        # for line in f:
        #     copy.write(line)
'''
with open("test.txt", 'a') as f:
    f.write("test line from append\n")
    # f.seek(0)
    # f.write("I'M WRITING FROM THE START!!!!!!!!!\n")

with open("test.txt", 'r+') as f:
    print(f.read())
    f.write("new line from r+")
    f.seek(0)
    f.write("I'M WRITING FROM THE START!!!!\n")
    print(f.read())

with open("test.txt", 'a+') as f:
    f.write("test line from a+")
    f.seek(0)
    f.write("I'M APPENDING FROM THE START!!!!\n")
    print(f.read())

with open("test.txt", 'w+') as f:
    f.write("this file was empty")
    f.seek(0)
    print(f.read())
    '''