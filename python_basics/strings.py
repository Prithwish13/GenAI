tea_type = "Masala Chai"
customer_name = "priya"

print(f"Serving {tea_type} to {customer_name}")

description = "Aromatic and spicy"
print(f"first word of description: {description.split(" ")[0]} and last character: {description[12:]}")

print(f"reversed description: {description[::-1]}")

label_text = "cafe chai§§ ¸¸"
encoded_label = label_text.encode("utf-8")
print(f"encoded label: {encoded_label}")
print(f"actual label: {label_text}")

decoded_label = encoded_label.decode("utf-8")
print(f"decoded label: {decoded_label}")
