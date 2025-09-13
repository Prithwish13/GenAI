class simple_chai:
    def __init__(self):
        self.origin = "India"
        
    def display_origin(self):
        print(f"Chai originates from {self.origin}")


chai = simple_chai() # each object has its own namespace and its own copy of attributes
chai.display_origin()