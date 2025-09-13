class Tea:
    temperature = "Hot"  # class attribute
    strength = "Strong"  # class attribute
    
cutting = Tea()
print(f"Cutting Tea is served {cutting.temperature} and is {cutting.strength}.")

cutting.temperature = "Warm"  # instance attribute
cutting.strength = "Mild"     # instance attribute

print(f"Cutting Tea is served {cutting.temperature} and is {cutting.strength}.")

print(f"Class attribute Temperature: {Tea.temperature} and Strength: {Tea.strength}")

del cutting.temperature  # deleting instance attribute

print(f"Cutting Tea is served {cutting.temperature} and is {cutting.strength}.")