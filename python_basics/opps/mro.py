# Method Resolution Order

class A:
    label = "Class A"
    
class B(A):
    label = "Class B"
    
class C(A):
    label = "Class C"
    
    
class D(B, C):
    pass

cup = D()
print(cup.label)  # Output: Class B

print(D.__mro__)  # Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
print(D.mro())    # Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]