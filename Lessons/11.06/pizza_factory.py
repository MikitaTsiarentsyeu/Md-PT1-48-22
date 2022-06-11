def prepare():
    print("STARTING NEW PIZZAMAKING PROCESS")
    print("preparing a base")
    print("choosing a sauce")

def add_ingridinent(ingridient):
    print(f"adding {ingridient}")

def griding_cheese():
    print("griding cheese")

def bake(time):
    print(f"baking for a {time} minutes")

def done():
    print("slicing")
    print("boxing")
    print("done!")

# def make_peperonni():
#     prepare()
#     add_ingridinent("peperonni")
#     griding_cheese()
#     bake(15)
#     done()

# def make_double_peperonni():
#     prepare()
#     add_ingridinent("peperonni")
#     add_ingridinent("peperonni")
#     griding_cheese()
#     bake(15)
#     done()

# def make_4_cheeses():
#     prepare()
#     add_ingridinent("mozarella")
#     add_ingridinent("chedder")
#     add_ingridinent("feta")
#     add_ingridinent("quatrochento")
#     bake(10)
#     done()

def maker(ingridients:list, time_to_bake:int, grinding:bool):
    def inner():
        prepare()
        for i in ingridients:
            add_ingridinent(i)
        if grinding:
            griding_cheese()
        bake(time_to_bake)
        done()
    return inner

make_peperonni = maker(["peperonni"], 15, True)
make_double_peperonni = maker(["peperonni", "peperonni"], 15, True)
make_4_cheeses = maker(["mozarella", "chedder", "feta", "quatrochento"], 10, False)

make_peperonni()
make_double_peperonni()
make_4_cheeses()

# l = ["peperonni", "peperonni"]
# mdp = maker(l, 15, True)
# del l[0]
# mp = maker(l, 15, True)

# mdp()

