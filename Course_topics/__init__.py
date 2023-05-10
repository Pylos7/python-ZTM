# Nestor Ingles
# OOP
class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, name, age):  # Constructor
        self.name = name    # Attributes
        self.age = age

    def shout(self):  # Method
        print(f"My name is {self.name}")

    # Class Method - Can be used without instantiating the class - Uses class attributes
    @classmethod
    def adding_things(cls, num1, num2):
        return cls("Teddy", num1 + num2)

    # Static Method - Can be used without instantiating the class - Uses no class attributes
    @staticmethod
    def adding_things(num1, num2):
        return num1 + num2


# player1 = PlayerCharacter('Tom', 10)  # Instantiation
player3 = PlayerCharacter.adding_things(2, 3)
print(player3.age)
