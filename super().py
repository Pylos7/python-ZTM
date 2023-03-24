# 4 PILLARS OF OOP
    # 1. Inheritance
    # 2. Encapsulation
    # 3. Abstraction
    # 4. Polymorphism

class User(): # Parent class
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')


class Wizard(User): # Child class
    def __init__(self, name, power, email):
        super().__init__(email) # super() is used to inherit the parent class attributes
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


wizard1 = Wizard("Merlin", 50, "merlin@gmail.com")

print(wizard1.email)