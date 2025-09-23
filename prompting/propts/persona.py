# Persona based prompting
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client = OpenAI()


system_prompt="""
    You are an AI persona Assistant named Prithwish Dey.
    You are acting behalf of Prithwish who is 29 years old software engineer tech stack is full stack development in MERN & MEAN stack
    
    examples:
    Q: Hey
    A: Hi! how are you?
"""
response = client.chat.completions.create(
        model="gpt-4o",
        messages= [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": "Hey there! who are you?"}
        ]
    )

print(response.choices[0].message.content)