class TeaBase:
    def __init__(self, tea_type):
        self.tea_type = tea_type

    def display_type(self):
        print(f"This is a {self.tea_type} tea.")
        
    def brew(self):
        print(f"Brewing the {self.tea_type} tea.")
        
        
class GreenTea(TeaBase):
    def __init__(self):
        super().__init__("Green")
        
    def brew(self):
        print("Steeping the green tea leaves in hot water for 2-3 minutes.")
        
base_tea = TeaBase("Black")
# base_tea.display_type()
# base_tea.brew()

green_tea = GreenTea()
# green_tea.display_type()
# green_tea.brew()

# Composition example
class TeaShop:
    tea_cls = TeaBase  # class attribute
    
    def __init__(self):
        self.tea = self.tea_cls("Herbal")
    
    def serve_tea(self):
        self.tea.display_type()
        self.tea.brew()
        print("Serving the tea.")
        
shop = TeaShop()
# shop.serve_tea()

class FancyTeaShop(TeaShop):
    tea_cls = GreenTea  # overriding class attribute to use GreenTea
    def __init__(self):
        self.tea = self.tea_cls()
    
fancy_shop = FancyTeaShop()

fancy_shop.serve_tea()
shop.serve_tea()   