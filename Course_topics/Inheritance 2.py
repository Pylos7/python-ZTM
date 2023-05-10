class User(): # Parent class
    def sign_in(self):
        print('logged in')

class Wizard(User): # Child class
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User): # Child class
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left- {self.num_arrows}')

wizard1 = Wizard("Merlin", 50)

print(isinstance(wizard1, object)) # True