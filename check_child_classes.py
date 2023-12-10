class Part: pass

class Segment(Part): pass

class Component(Segment): pass

class Car(Component): pass

class Industry(Car): pass

print(Part.__subclasses__())