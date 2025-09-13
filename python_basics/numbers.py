# Integer

import sys

black_tea_grams = 14
ginger_grams = 2

total_grams = black_tea_grams + ginger_grams
print(f"Total grams: {total_grams}")

# Float
milk_litres = 7
servings =4
milk_per_serving = milk_litres / servings
print(f"Milk per serving: {milk_per_serving} litres")

total_tea_bags =7
pots =4
bags_per_pot = total_tea_bags // pots
print(f"Bags per pot: {bags_per_pot}")


total_cardamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cardamom_pods % pods_per_cup

print(f"Leftover pods: {leftover_pods}")  


base_flavor_strength = 2
scale_factor = 3
powerful_flavor_strength = base_flavor_strength ** scale_factor
print(f"Powerful flavor strength: {powerful_flavor_strength}")

# Real numbers
ideal_temp = 95.5
current_temp = 95.499999999999

print(f"Ideal temperature: {ideal_temp}")
print(f"Current temperature: {current_temp}")
print(f"the difference is: {ideal_temp - current_temp}")

print(sys.float_info)
