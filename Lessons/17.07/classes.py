class Student:

    def __init__(self, name, year, speciality):
        self.set_name(name)
        self.year = year
        self.speciality = speciality

    def get_name(self):
        return self.__name.upper()

    def set_name(self, name):
        if name != "":
            self.__name = name

    name = property(get_name, set_name)

    def provide_info(self):
        print(f"I'm {self.get_name()}, {self.speciality} studdent of {self.year} year")

    def __learn__(self):
        print("I'm learning!")

s1 = Student("Mikita", 5, 'cake making')
# s1.name = "Mikita"
# s1.set_name("Mikita")
# s1.year = 5
# s1.speciality = "cake making"

s1.provide_info()
print(s1.name)
s1.name = "new name"

s2 = Student("Vasya", 3, 'metal bending')
s2.__learn__()

# Student.provide_info(s1)