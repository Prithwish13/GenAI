from pydantic import BaseModel, field_validator, model_validator
from datetime import datetime



class person(BaseModel):
    first_name: str
    last_name: str
    
    @field_validator('first_name', 'last_name')
    def names_must_be_alpha(cls, value):
        if not value.istitle():
            raise ValueError('Names must be capitalized')
        return value
    
    
class User(BaseModel):
    email: str
    
    @field_validator('email')
    def normalize_email(cls, v):
        return v.lower().strip()
    

user1 = User(email='DEYABIR30@GMAIL.COM ')
print(user1)


class Product(BaseModel):
    price: str
    
    @field_validator('price', mode='before')
    def parse_price(cls, v):
        if isinstance(v, str):
            return float(v.replace('$', ''))
        return v
    
    
class DateRange(BaseModel):
    start_date: datetime
    end_date: datetime
    
    @model_validator(mode='after')
    def check_date_order(cls, v):
        if v.end_date <= v.start_date:
            raise ValueError('end_date must be after start_date')
        return v

    
