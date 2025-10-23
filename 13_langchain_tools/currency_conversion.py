import os
import json
import requests
from langchain.tools import tool
from langchain_core.tools import InjectedToolArg
from typing import Annotated
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, ToolMessage, AIMessage


load_dotenv()

API_KEY = os.getenv('EXCHANGE_RATE_API_KEY')

@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
    """This function fetches the currency conversion factor between base and target currency"""
    uri = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{base_currency.upper()}/{target_currency.upper()}"
    response = requests.get(url=uri)
    return response.json()


@tool
def convert(base_currency_value: float, conversion_rate: Annotated[float, InjectedToolArg])->float:
    """This function will convert the base currency value with current conversion rate"""
    return base_currency_value * conversion_rate


llm = ChatOpenAI(model='gpt-4.1')

enhanced_llm = llm.bind_tools([get_conversion_factor, convert])

messages = [
    HumanMessage("What is the current conversion ratio between USD and INR, base on that convert 10 USD to INR")
]

ai_message = enhanced_llm.invoke(messages)

messages.append(ai_message)

print(ai_message.tool_calls)

cv_rate = None

for tool_call in ai_message.tool_calls:
    if tool_call['name'] == 'get_conversion_factor':
        tool_msg1 = get_conversion_factor.invoke(tool_call)
        cv_rate = json.loads(tool_msg1.content)['conversion_rate']
        messages.append(tool_msg1)
    if tool_call['name'] == 'convert':
        tool_call['args']['conversion_rate'] = cv_rate
        tool_msg2 = convert.invoke(tool_call)
        messages.append(tool_msg2)
        
print("till here evenrt thing is cool-----------------------", messages)
        
final_response = enhanced_llm.invoke(messages)

print(final_response.content)
    







    


