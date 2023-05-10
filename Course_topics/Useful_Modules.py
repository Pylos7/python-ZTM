# Usefull Methods

from collections import Counter, defaultdict, OrderedDict

# Counter - Helps with optimization problems, counting the number of times an element appears in a list
li = [1,2,3,4,5,6,7,7]
print(Counter(li)) # Counts the number of times each element appears in the list

sentence = 'blah blah blah thinking about python'
print(Counter(sentence)) # Counts the number of times each letter appears in the sentence



# defaultdict - Helps with optimization problems, when you want to use a dictionary but don't want to worry about key errors
dictionary = defaultdict(lambda: 'does not exist', {'a': 1, 'b': 2})
print(dictionary['b']) # Prints 1



# OrderedDict - Helps with optimization problems, when you want to use a dictionary but want to keep the order of the keys


d1 = {'c': 100}
d1['a'] = 1
d1['b'] = 2

d2 = {'c': 100}
d2['b'] = 2
d2['a'] = 1


# Note: A recent python update has made dictionaries ordered by default, so this is not as useful as it used to be


d3 = OrderedDict()
d3['a'] = 1
d3['b'] = 2

d4 = OrderedDict()
d4['b'] = 2
d4['a'] = 1

print(d1 == d2) # Prints True
print(d3 == d4) # Prints False