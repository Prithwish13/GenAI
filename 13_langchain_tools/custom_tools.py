
# Using LangChain's @tool decorator to create a custom multiplication tool

from langchain.tools import tool

@tool
def multiply(a: int, b: int) -> int:
    """Multiplies multiple numbers"""
    return a * b

result = multiply.invoke({'a': 5, 'b': 6})
print(result)  
print(multiply.description)
print(multiply.name)
print(multiply.args)


# Using structured tool 
from langchain.tools import StructuredTool
from pydantic import BaseModel, Field


class MultiplyInput(BaseModel):
    a: int = Field(..., description="The first number to add")
    b: int = Field(..., description="The second number to add")
    

def add_func(a: int, b: int) -> int:
    return a + b 

add_tool = StructuredTool.from_function(
    func=add_func,
    name='addition',
    description='Add two numbers',
    args_schema=MultiplyInput
)

add_result = add_tool.invoke({'a': 3, 'b': 7})

print(add_result)

# From Base tool class
from langchain.tools import BaseTool
from typing import Type

class SubtractionInput(BaseModel):
    a: int = Field(..., description="The first number to subtract")
    b: int = Field(..., description="The second number to subtract")
    
class SubtractTool(BaseTool):
    name: str = 'subtract_emo'
    description: str = 'this function will perform subtraction of two numbers'
    
    args_schema: Type[BaseModel] = SubtractionInput
    
    # can make async function of the tools
    def _run(self, a: int, b: int) -> int:
        return a - b
    
sub_tool = SubtractTool()

sub_res = sub_tool.invoke({'a': 79900, 'b': 35000})

print(sub_res)


# merging them all and making tool kit