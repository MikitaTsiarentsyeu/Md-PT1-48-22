class Food:

    def __init__(self, name, type) -> None:
        self.name = name
        self.type = type
    
    def __str__(self) -> str:
        return self.name

class Animal:

    def __init__(self, name) -> None:
        self.__name = name

    def eat(self, some_food:Food):
        print(f"eating {some_food}")

    def phe(self):
        print("phe...")

    def get_name(self):
        return self.__name

    name = property(get_name)

class Carnivore(Animal):

    def eat(self, some_food: Food):
        if some_food.type == "meat":
            Animal.eat(self, some_food)
        else:
            super().phe()

class Herbivore(Animal):

    def eat(self, some_food: Food):
        if some_food.type == "herbal":
            Animal.eat(self, some_food)
        else:
            super().phe()

class Omnivore(Carnivore, Herbivore):

    def eat(self, some_food: Food):
        if some_food.type == "meat":
            Carnivore.eat(self, some_food)
        elif some_food.type == "herbal":
            Herbivore.eat(self, some_food)
        else:
            self.phe()


steak = Food("steak", "meat")
grass = Food("grass", "herbal")
stone = Food("stone", "stone")

food_package = [steak, grass, stone]

dog = Carnivore("Zephyrka")
cow = Herbivore("Myrka")
human = Omnivore("Vasya")

eaters = [dog, cow, human]

for food in food_package:
    for eater in eaters:
        print(eater.name)
        eater.eat(food)

# dog.eat(steak)
# human.eat(steak)

# dog.eat(grass)
# human.eat(grass)


class Cat:

    def hello(self):
        print("Hello, I'm a cat")


class Dog:

    def hello(self):
        print("Hello, I'm a dog")

l = [Cat(), Dog()]
for a in l:
    a.hello()