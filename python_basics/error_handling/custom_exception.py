
# Raise a custom error
def brew_chai(flavor):
    if flavor not in ["masala", "ginger", "cardamom"]:
        raise ValueError(f"Unknown flavor: {flavor}")
    print(f"Brewed a cup of {flavor} chai!")
    
    
    
try:    brew_chai("mint")
except ValueError as e:
    print(f"Custom Exception caught: {e}")

# custom exception class
class OutOfIngredientsError(Exception):
      pass
  
  
def makeTea(milk, sugar):
    if milk < 50:
        raise OutOfIngredientsError("Not enough milk to make tea.")
    if sugar < 10:
        raise OutOfIngredientsError("Not enough sugar to make tea.")
    print("Tea is ready!")
    
makeTea(30, 9)  # This will raise OutOfIngredientsError