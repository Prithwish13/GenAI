from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True
    
# Right way 
product_one = Product(id=1, name="Laptop", price=900, in_stock=True)

product_two = Product(id=2, name="Smart Phone", price=500, in_stock=True)


