from openai import OpenAI
from dotenv import load_dotenv
import requests

load_dotenv()

client = OpenAI()

def get_weather(city: str):
    weather_url=f"https://wttr.in/{city.lower}?format=%c+%t"
    response = requests.get(weather_url)
    print(response)
    
    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"

def main():
    user_query = input("👉 ")
    response = client.chat.completions.create(
        model='gpt-4o',
        messages=[
            { 'role': 'user', 'content': user_query}
        ]
    )
    print(f"🤖: {response.choices[0].message.content}")
    
main()



# Weather API Call 'https://wttr.in/{city}?format=%c+%t'