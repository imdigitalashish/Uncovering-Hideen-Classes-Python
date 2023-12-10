'''

__getattr__ -> This will be called only when the attribute is not found

__getattribute__ -> This will be called everytime when you're trying to access the attribute

'''
class Car:
    def __init__(self, model):
        self.model = model

    def __getattr__(self, key):
        return f"{key} not found"
    
    

car = Car(model="Tesla")

print(car.model)
print(car.trash)




class Car:
    def __init__(self, model):
        self.model = model

    def __getattribute__(self, key):
        return f"{key} not found"
    
    

car = Car(model="Tesla")

print(car.model)
print(car.trash)