

def init(self,name,model):
    self.name = name
    self.model = model

def Bhrooom(self):
    print("VRRROM VROOOOOOM")

Car = type('Car', (), {'__init__': init, 'vroom': Bhrooom})

car = Car("Tesla", "x86")
car.vroom()