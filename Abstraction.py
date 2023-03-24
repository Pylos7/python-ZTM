# 4 PILLARS OF OOP
    # 1. Inheritance
    # 2. Encapsulation
    # 3. Abstraction
    # 4. Polymorphism

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("run")

    def speak(self):
        print(f"My name is {self.name}, and I am {self.age} years old")

player1 = PlayerCharacter("Nestor", 30)
player1.speak()
print((1,2,3,1).count(1))
player1.name = "!!!"
player1.speak = "BOOOOOO" # Overriding the method = BAD PRACTICE
# You have use of things whithout knowing how they work
# You can use the count method of a tuple without knowing how it works
# You can use the speak method of a PlayerCharacter object without knowing how it works

print(player1.speak) 