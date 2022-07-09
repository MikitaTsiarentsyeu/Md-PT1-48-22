class Simpleton: pass

print(Simpleton, type(Simpleton))

s = Simpleton()
print(s, type(s))

s2 = Simpleton()

s.test = 4
print(s.test)

Simpleton.test = 77
print(Simpleton.test, s2.test, s.test)

Simpleton.test = 88
print(Simpleton.test, s2.test, s.test)

s2.test = 5
print(Simpleton.test, s2.test, s.test)


class Student:

    __name = ""
    year = 0
    speciality = ""

    def get_name(self):
        return self.__name.upper()

    def set_name(self, name):
        if name != "":
            self.__name = name

    def provide_info(self):
        print(f"I'm {self.get_name()}, {self.speciality} studdent of {self.year} year")

    def __learn__(self):
        print("I'm learning!")

s1 = Student()
# s1.name = "Mikita"
s1.set_name("Mikita")
s1.year = 5
s1.speciality = "cake making"

s1.provide_info()
print(s1._Student__name)
# s1.name = ""

s2 = Student()
s2.set_name("Vasya")

s2.__learn__()

# Student.provide_info(s1)