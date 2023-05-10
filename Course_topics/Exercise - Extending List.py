# Exercise: Extending List

class SuperList(list): # Inherit from list
    def __len__(self):
        return 1000
    
super_list1 = SuperList()

print(len(super_list1)) # 1000
super_list1.append(5) # AttributeError: 'SuperList' object has no attribute 'append'
print(super_list1[0]) # IndexError: list index out of range
print(issubclass(SuperList, list)) # True