import requests
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

load_dotenv()
weather_stack_key=os.getenv('WEATHER_STACK_API_KEY')

search_tool = DuckDuckGoSearchRun()
llm = ChatOpenAI(model_name="gpt-4.1", temperature=0)

@tool
def get_weather_data(city: str) -> str:
    """
        this function fetches the current weather data for a given city
    """
    weather_url=f"http://api.weatherstack.com/current?access_key={weather_stack_key}&query={city}"
    response = requests.get(weather_url)
        
    return response.json()


# Pull the ReAct prompt from the Langchain Hub
prompt = hub.pull('hwchase17/react')

# creating the agent

agent = create_react_agent(
    llm=llm,
    tools=[search_tool, get_weather_data],
    prompt=prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool, get_weather_data],
    verbose=True # Printing the plannings of agents
)

result = agent_executor.invoke({
    'input': 'find the capital of west bengal and its current weather condition'
})

print(result)

