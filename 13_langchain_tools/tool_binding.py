from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage, AIMessage
from dotenv import load_dotenv
import requests


load_dotenv()

@tool
def multiply(a: int, b: int) -> int:
    """Multiplies multiple numbers"""
    return a * b

llm = ChatOpenAI(model_name="gpt-4.1", temperature=0)
llm_with_tools = llm.bind_tools([multiply])
messages = [
     HumanMessage(content="What is the product of 7 and 8? Use the multiply tool to calculate it.")
]

response = llm_with_tools.invoke(messages)
messages.append(response)

# tool execution
tool_res = multiply.invoke(response.tool_calls[0])
messages.append(tool_res)

final_response = llm_with_tools.invoke(messages)

print(f"the final answer is, {final_response.content}")
