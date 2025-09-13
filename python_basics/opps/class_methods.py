class TeaOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size
        
    @classmethod
    def from_dic(cls, order_data):
        return cls(
            tea_type=order_data.get("tea_type", "Black"),
            sweetness=order_data.get("sweetness", "Medium"),
            size=order_data.get("size", "Medium")
        )
    
    @classmethod
    def from_string(cls, order_str):
        tea_type, sweetness, size = order_str.split("-")
        return cls(tea_type, sweetness, size)
    
class TeaUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ["Small", "Medium", "Large"]
    
    
print(TeaUtils.is_valid_size("Medium"))  # True
    
order1 = TeaOrder.from_dic({"tea_type": "Oolong", "sweetness": "Low", "size": "Large"})
order2 = TeaOrder.from_string("Green-High-Small")

print(order1.tea_type, order1.sweetness, order1.size)  # Oolong Low Large
print(order2.tea_type, order2.sweetness, order2.size)  # Green High Small

print(order1.__dict__)
