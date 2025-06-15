from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = "Unknown" # Default value for name
    age: Optional[int] = None # Optional field with default value None
    # email: EmailStr
    cgpa:  float = Field( gt=0.0, le=10.0, default=4, description='decimal value representing cgpa') # CGPA must be between 0.0 and 10.0
    
new_student = {'name': 'Prithwish', 'email': 'abc@gmail.com', 'cgpa': 10 }

student = Student(**new_student)
std_dict = dict(student)

print(std_dict['name'])