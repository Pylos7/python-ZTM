# Multiple Inheritance

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

    def check_arrows(self):
        print(f'{self.num_arrows} remaining')

    def run(self):
        print('ran really fast')


class HybridBorg(Wizard, Archer): # Gets all methods from both parent classes
    def __init__(self, name, power, num_arrows):
        Archer.__init__(self, name, num_arrows)
        Wizard.__init__(self, name, power)

hb1 = HybridBorg('borgie', 50, 100)
print(hb1.check_arrows())