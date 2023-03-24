# 4 PILLARS OF OOP
    # 1. Inheritance
    # 2. Encapsulation
    # 3. Abstraction
    # 4. Polymorphism

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age


player1 = PlayerCharacter("Nestor", 30)
print(player1.name)
print(player1.age)

player2 = {"name" : "Miguel Angel", "age" : 26}
print(player2["name"])
print(player2["age"])