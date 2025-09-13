# immutable data types: int, float, bool, str, tuple

sugar_amount = 2

print(f"Initial sugar amount: {sugar_amount} and Id: {id(sugar_amount)}")

sugar_amount = 10

print(f"Updated sugar amount: {sugar_amount} and Id: {id(sugar_amount)}")

# mutable data types: list, dict, set

ingredients = ["water", "tea leaves", "sugar"]
print(f"Initial ingredients: {ingredients} and Id: {id(ingredients)}")
ingredients.append("milk")
print(f"Updated ingredients: {ingredients} and Id: {id(ingredients)}")
# Example of tuple (immutable)
dimensions = (5, 10)
print(f"Dimensions: {dimensions} and Id: {id(dimensions)}")

#set example
spice_mix = set()
print(f"Initial spice mix: {spice_mix} and Id: {id(spice_mix)}")
spice_mix.add("cardamom")
print(f"Updated spice mix: {spice_mix} and Id: {id(spice_mix)}")