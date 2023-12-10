class Car:

    def __init__(self, name):
        self.name = name
      

class Model(Car):

    def __init__(self, name, model):
        Car.__init__(self, name) # or super().__init__(name)
        self.model = model

car = Model("Tesla", "x86")