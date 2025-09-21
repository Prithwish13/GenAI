def process_order(item, quantity):
    try:
        price = {"masala": 50, "ginger": 40, "green": 60}[item]
        total = price * quantity
        print(f"Total price for {quantity} cups of {item} tea is: {total}")
        
    except KeyError as e:
        print(f"KeyError caught: {e} - Item not found in the menu.")
    except TypeError as e:
        print(f"TypeError caught: {e} - Invalid type for quantity.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Finished processing the order.")
        
process_order("masala", 2)  # Valid case
process_order("herbal", 2)   # This will raise a KeyError
process_order("ginger", "two")  # This will raise a TypeError