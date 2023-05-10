# 4 PILLARS OF OOP
    # 1. Inheritance
    # 2. Encapsulation
    # 3. Abstraction
    # 4. Polymorphism

class User(): # Parent class
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')

class Wizard(User): # Child class
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f'attacking with power of {self.power}')

class Archer(User): # Child class
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left- {self.num_arrows}')

wizard1 = Wizard("Merlin", 50)
archer1 = Archer("Robin", 30)

def player_attack(char):
    char.attack()

player_attack(wizard1)
player_attack(archer1)

for char in [wizard1, archer1]:
    char.attack()

print(wizard1.attack())