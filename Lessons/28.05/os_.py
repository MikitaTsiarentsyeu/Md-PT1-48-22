import os

print(os.name)

print(os.sep)

structure = ["level 1", "level 2", "level 3"]
print(os.sep.join(structure))

x = os.path.join(*structure)
print(x)

# os.makedirs(x)

# print(os.getcwd())
# os.chdir(x)
# print(os.getcwd())

print(os.listdir())

print(os.walk(os.getcwd()))
for item in os.walk(os.getcwd()):
    print(item)

print(os.removedirs(x))