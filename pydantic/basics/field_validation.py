from pydantic import BaseModel, field_validator, model_validator

class User(BaseModel):
    name: str
    age: int

    @field_validator('age')
    def check_age(cls, value):
        if value < 0:
            raise ValueError('Age must be a non-negative integer')
        return value
    
class SignupData(BaseModel):
    password: str
    confirm_password: str
    
    @model_validator(mode='after')
    def passwords_match(cls, values):
        if values.password != values.confirm_password:
            raise ValueError('Passwords do not match')
        return values
    
    
signup = SignupData(password='secret', confirm_password='secret')
print(signup)