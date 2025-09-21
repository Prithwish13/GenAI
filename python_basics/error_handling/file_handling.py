# file = open("order.text", "w")

# try:
#  file.write("Masala Tea- 2 cups")
 
# finally:
#     file.close()


# modern way

with open("order.txt", "w") as file:
    file.write("Ginger Tea - 4 cups")