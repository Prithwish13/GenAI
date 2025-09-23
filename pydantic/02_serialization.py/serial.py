from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: str
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime
    address: Address
    tags: List[str] = []
    
    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')
        } # just for modify datetime format!
    )
    

user = User(
    id="1",
    name="Prithwish",
    email="deyabir30@gmail.com",
    createdAt=datetime(2024, 3, 15, 14, 30),
    address=Address(
        street="Old Culcutta Road",
        city="Kolkata",
        zip_code="700115",
    ),
    tags=["Premium", "Subscriber"]
)

python_dict = user.model_dump()
json_str = user.model_dump_json()

print(python_dict)
print("="* 50)
print(json_str)