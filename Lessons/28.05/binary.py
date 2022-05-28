chunk_size = 1000

count = 0

with open('test.jpg', 'rb') as f:
    with open('test-copy.jpg', 'wb') as f_copy:
        chunk = f.read(chunk_size)
        while chunk:
            f_copy.write(chunk)
            count += 1
            chunk = f.read(chunk_size)
            
    # print(f.read())
    # print(f.readline())
    # print(len(f.readlines()))

print(count)