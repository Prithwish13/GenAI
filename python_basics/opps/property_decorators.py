class TeaLeaf:
    def __init__(self, age):
        self._age = age
        
    @property
    def age(self):
        return self._age + 1  # Simulating age increment for demonstration
    
    
    @age.setter
    def age(self, age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Tea Leaf age must be between 1 and 5 years.")
        
        
leaf = TeaLeaf(3)
print(leaf.age)  # Accessing age property, should print 4
leaf.age = 4     # Setting age property
print(leaf.age)  # Accessing age property, should print 5