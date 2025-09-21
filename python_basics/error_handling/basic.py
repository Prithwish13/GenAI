# 1. Out of index error
my_list = [1, 2, 3]

try:
    print(my_list[5])  # This will raise an IndexError
except IndexError as e:
    print(f"IndexError caught: {e}")
finally:
    print("Finished handling index error.")
    
    
    
print("Rest of the code is being executed...")