class Car1:
    def test(self):
        print("CAR 1")

class Car2:
    def test(self):
        print("CAR 2")

# This is known as the Method Resolution Order (MRO) in which Car1 is first inherited, so Car1.test() would be called if we switch Car2 first then Car 2 will be printed
class Showroom(Car1, Car2):
    pass

print(Showroom().test())