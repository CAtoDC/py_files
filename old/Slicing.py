# Slicing in Python

from collections import Sequence
 
class MyStructure(Sequence):
    def __init__(self):
        self.data = []
 
    def __len__(self):
        return len(self.data)
 
    def append(self, item):
        self.data.append(item)
 
    def remove(self, item):
        self.data.remove(item)
 
    def __repr__(self):
        return str(self.data)
 
    def __getitem__(self, sliced):
        return self.data[sliced]

# Test it
m = MyStructure()
m.append('First element')
print(m[0])

# Now add more elements
m.append('Second element')
m.append('Third element')

# Print all of them
print (m)

# Print the last two
print (m[1:3])
