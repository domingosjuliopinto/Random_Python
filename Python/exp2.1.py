#program to show class,object , inheritance, constructor ,method
class Car:          #parent class

    def __init__(self, name, mileage):
        self.name = name 
        self.mileage = mileage 

    def description(self):                
        print(self.name ,self.mileage)

class BMW(Car):     #child class
    pass

class Audi(Car):     #child class
    def audi_desc(self):
        return "This is the description method of class Audi."

print("Car   Mileage")

obj1 = BMW("BMW 7-series",39.53)
obj1.description()

obj2 = Audi("Audi A8 L",14)
obj2.description()
print(obj2.audi_desc())
