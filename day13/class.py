class Car:
    def __init__(self, wheels, sideMirrors, doors):
        self.wheels = wheels
        self.sideMirrors =  sideMirrors
        self.doors = doors

    def details(self):
        print(F"Wheels = {self.wheels}\n sidemirrors = {self.sideMirrors}\n doors = {self.doors}")

        

car1 = Car(4, 2, 6)
car1.details()

car2 = Car(5, 3, 2)
car2.details()