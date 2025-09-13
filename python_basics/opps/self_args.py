class Teacup:
    def __init__(self, color, shape):
        self.color = color  # instance variable
        self.shape = shape  # instance variable

    def display_info(self):
        print(f"This teacup is {self.color} and {self.shape} in shape.")
        
        
        
cup1 = Teacup("white", "round")
cup2 = Teacup("blue", "square")

cup1.display_info()
cup2.display_info()