from pydantic import BaseModel, computed_field, Field

class Product(BaseModel):
    name: str
    price: float
    tax: float = 0.2  # 20% tax by default

    @computed_field
    @property
    def price_with_tax(self) -> float:
        return self.price * (1 + self.tax)
    
product = Product(name='Laptop', price=1000)
print(product)

class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(..., gt=0)
    rate_per_night: float = Field(..., gt=0)
    
    @computed_field
    @property
    def total_amount(self) -> float:
        return self.nights * self.rate_per_night


booking = Booking(user_id=1, room_id=101, nights=3, rate_per_night=150)
print(booking)