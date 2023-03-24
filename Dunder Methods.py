# Dunder Methods

class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False
        }

    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    def __call__(self):
        return('yes??')

    def __getitem__(self, i):
        return self.my_dict[i]
    
action_figure = Toy('red', 0)
print(action_figure.__str__()) # Same as below
print(str(action_figure)) # __str__ is called automatically
print(len(action_figure)) # __len__ is called automatically
print(action_figure()) # __call__ is called automatically
print(action_figure['name']) # __getitem__ is called automatically
