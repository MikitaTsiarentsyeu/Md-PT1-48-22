for i in range(10):
    i += 1

print(i)

[i + 1 for i in range(100)]

print(i)

def func1():
    print("this is func1")

def func2():
    print("this is func2")
    func1()


x, y = "x global val", "y global val"

def test_args(x, y):
    print(x, y)

test_args(2,3)
print(x, y)

x = "global value"

test = "also global value"

def scope_test():
    # print(f"scope_test 1 x - {x}") error
    x = '44'
    print(f"scope_test 2 x - {x}")

print(f"global 1 x - {x}")
scope_test()
print(f"global 2 x - {x}")

x = [1]

def test_list_scope():
    # del x error
    print(f"test_list_scope 1 x - {x}")
    x.append(2)
    print(f"test_list_scope 1 x - {x}")

print(f"global 1 x - {x}")
test_list_scope()
print(f"global 2 x - {x}")

x = 100

def test_global_1():
    x = 200 #it will be local
    print(f"test_global_1 - {x}")

def test_global_2():
    global x
    x = 300
    print(f"test_global_2 - {x}")

def test_global_3():
    print(f"test_global_3 - {x}")

test_global_1()
test_global_2()
test_global_3()
print(x)

val = 5

def fun1():
    val = 3
    def fun2():
        global val
        val = 8
        print(val)
    fun2()
    print(val)

fun1()
print(val)

def test_local_level1():
    val = 3
    def test_local_level2():
        nonlocal val
        val = 12
        print(val)
        def test_local_level3():
            nonlocal val
            val = 15
            print(val)
        test_local_level3()
        print(val)
    test_local_level2()
    print(val)

test_local_level1()
print(val)
