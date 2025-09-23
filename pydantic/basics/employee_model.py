from typing import Optional
from pydantic import BaseModel, Filed
import re

class Employee(BaseModel):
    id: int
    name: str = Filed(
        ..., # this denoted that require field
        min_length=3,
        max_len=50,
        description="Employee Name",
        examples="Prithwish Dey"
    )
    department: Optional[str]= 'General'
    salary: float = Filed(
        ...,
        ge=10000,
        description="Annual salary in usd"
    )
    
class User(BaseModel):
    email: str= Filed(
        ...,
        regex=r''
    )
    age:int = Filed(
        ...,
        ge=0,
        le=150,
        description="Age in years"
    )
    discount: float=Filed(
        ...,
        ge=0,
        le=100,
        description="Discount Percentage"
    )
    
    
    
