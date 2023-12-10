class Car:

    def __add__(self, x):
        return "adding to car: " + str(x)

    def __sub__(self,x ):
        return "orange"

    # After Reversed  
    def __radd__(self, x):
        return f"Adding car to: {str(x)} "
    
    def __rsub__(self, x):
        return f"Subtracting car to: {str(x)}"
    

car = Car()

print(2+ car)