x = "test value"
y = 'test value'

print(x == y)
 

x = "test value color='red'"
y = 'test value color="red"'
z = 'test value color=\'red\''

print(x == y)

x = """line 1
    line 2
        line 3"""
print(x)