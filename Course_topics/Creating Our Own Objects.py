# OOP
class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, name, age):  # Constructor
        if (self.membership):
            self.name = name    # Attributes
            self.age = age

    def shout(self):  # Method
        print(f"My name is {self.name}")

    def run(self):  # Method
        print("run")


player1 = PlayerCharacter('Cindy', 87)  # Instantiation
player2 = PlayerCharacter('Tom', 12)  # Instantiation

print(player1.name + " is " + str(player1.age) + " years old.")
print(player2.name + " is " + str(player2.age) + " years old.")

print(player1.shout())
print(player2.shout())
