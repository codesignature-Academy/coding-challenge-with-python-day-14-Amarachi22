'''
create a dog class
using the constructor accept name,age. strngth = 10

create a method play -1, sleep + 1, eat +1
if strngth is <5 print(WEAK)
elif strength >= 7 tired else strong

note: constructor is the init thunder that is use to cre
'''

class Dog:
    def __init__(self, name, age, strength = 10):
        self.name = name
        self.age = age
        self.strength = strength

    def play(self):
        if self.strength > 1:
            self.strength -= 1


    def sleep(self):
        if self.strength != 10:
            self.strength += 1

    def eat(self):
        if self.strength <= 7:
            self.strength += 3

    def check_strength(self):
        if self.strength < 5:
            print(f"{self.name} is weak\n {self.strength}")
        elif self.strength <= 7:
            print(f'{self.name} is tired\n {self.strength}')
        else:
            print(f"{self.name} is strong\n {self.strength}")
       
dog1 = Dog("bruno", 3)
dog1.play()   
dog1.play()   
dog1.play()   

dog1.eat()
dog1.check_strength()



