tea_order = dict(type="Masala Chai", sugar_level="Less Sugar", tea_strength="Strong")

print(tea_order)

tea_recipe = {}

tea_recipe["base"] = "black tea"
tea_recipe["liquid"] = "milk"

print(f"tea recipe: {tea_recipe}")

del tea_recipe["liquid"]

print(f"tea recipe after deleting: {tea_recipe}")


print(f"is sugar_level in tea_order? {'sugar_level' in tea_order}")


new_order = {"type": "Ginger Tea", "sugar_level": "No Sugar", "tea_strength": "Light"}

# print(f"Order details keys: {new_order.keys()}")
# print(f"Order details value: {new_order.values()}")
# print(f"Order details items: {new_order.items()}")

last_item = new_order.popitem()
print(f"Removed item: {last_item}") 

extra_spices = {"spices": ["ginger", "cardamom"]}

new_order.update(extra_spices)
print(f"Updated order: {new_order}")

spices = new_order.get("spices")
notfound = new_order.get("spics") # returns None if key not found
print(f"Spices in the order: {spices} and notfound: {notfound}")