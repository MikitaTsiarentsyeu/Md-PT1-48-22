
x = 150

if x > 100:
    print("It's a huge number")
elif x < 100:
    print("Not so huge")
else:
    print("it's 100")



x = 3

if x == 1:
    print("one")
elif x == 2:
    print("two")
elif x == 3:
    print("three")
elif x == 4:
    print("four")
elif x == 5:
    print("five")
    
x = -3

if x > 0:
    print("positive")
elif x == 0:
    print("zero")
else:
    print("negative")

if x >= 0:
    if x == 0:
        print("zero")
    else:
        print("postive")
else:
    print("negative")


print("it's true") if False else print("it's false")
x = "true" if False else "false"
print(x)

print("positive") if x > 0 else print("zero") if x == 0 else print("negative")

print("the end")