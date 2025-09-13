import sys

class Chai:
    def __init__(self, sweetness, milk_level):
        self.sweetness = sweetness
        self.milk_level = milk_level
    
    def sip(self):
        print("Sipping Chai", sys.version)
    
    def add_milk(self):
        print("Adding milk to Chai")
        
my_tea = Chai(sweetness="medium", milk_level="high")

my_tea.sip()
my_tea.add_milk()