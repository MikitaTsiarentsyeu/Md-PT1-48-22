from ctypes import ArgumentError


class FreightTrain:

    __cart_len = 10

    def __init__(self, cart_count) -> None:
        self.cart_count = cart_count

    def __str__(self) -> str:
        return f"I'm a train of {self.cart_count} carts, choo-choo!"

    def __int__(self):
        return self.cart_count

    def __add__(self, other):
        try:
            return FreightTrain(self.cart_count + other.cart_count)
        except:
            raise ArgumentError("cannot add non-FreightTrain object")

    def __eq__(self, __o) -> bool:
        if not isinstance(__o, FreightTrain):
            return False

        return self.cart_count == __o.cart_count

    def __len__(self):
        return self.cart_count * self.__cart_len


loooooong = FreightTrain(25)
shorty = FreightTrain(3)

print(loooooong)
print(shorty)

print(int(shorty))

print(loooooong+shorty)
print(loooooong == shorty)
print(loooooong+shorty==FreightTrain(28))

print(len(loooooong))