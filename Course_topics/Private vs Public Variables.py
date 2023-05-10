# Private?
class PlayerCharacter:
    def __init__(self, name, age): # Dunder method
        self._name = name
        self._age = age

    def run(self):
        print("run")

    def speak(self):
        print(f"My name is {self._name}, and I am {self._age} years old")

player1 = PlayerCharacter("Nestor", 30)

player1.speak = "BOOOOOO" # Overriding the method = BAD PRACTICE


print(player1.speak)