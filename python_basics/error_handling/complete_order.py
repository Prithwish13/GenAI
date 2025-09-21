class InvalidTeaError(Exception):
    """Custom exception for invalid tea orders."""
    pass


def bill(flavour, cups):
    menu = {"masala": 20, "ginger": 15, "milk": 12}
    try:
        if flavour not in menu:
            raise InvalidTeaError("This Tea is not available")
        if not isinstance(cups, int):
            raise TypeError("Cups contains an invalid type")
        
        total = menu[flavour] * cups
        
        print(f"Your bill for {cups} cups of {flavour} chai: rupees {total}")
        
    except Exception  as e:
        print("Error: ", e)
    
    finally:
        print("Thank you visit again")
        
bill("ginger", 2)
bill("black", 2)
bill("masala", "Two")
    