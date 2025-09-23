from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": "You are a maths expert! only answer the math related questions. If the query is not related to maths then simply say that Sorry! I only can answer math related questions"
        },
        {
            "role": "user",
            "content": "what is the dictionary in python"
        }
    ]
)

print(response.choices[0].message.content)