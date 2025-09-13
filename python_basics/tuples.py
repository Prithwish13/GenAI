spices = ("cinnamon", "nutmeg", "clove", "ginger")


(spice1, spice2, *rest) = spices

print(spice1)
print(spice2)
print(rest)

cinnamon_ratio, clove_ratio =  2, 1

# swap values
cinnamon_ratio, clove_ratio = clove_ratio, cinnamon_ratio

print(f"Is ginger is available in masalas: {'ginger' in spices}")