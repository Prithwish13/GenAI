class Chai:
    
    def __init__(self, type_of_chai, strength):
        self.type_of_chai = type_of_chai
        self.strength = strength
        

class GingerChai(Chai):
    
    def __init__(self, type_of_chai, strength, spice_level):
        super().__init__(type_of_chai, strength)
        self.self_spice_level = spice_level
        
    