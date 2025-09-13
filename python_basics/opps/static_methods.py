class TeaUtils:
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]
    
    
    
    
cleaned = TeaUtils.clean_ingredients(" sugar, milk, lemon ")  # ['sugar', 'milk', 'lemon']

print(cleaned)