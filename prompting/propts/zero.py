from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

#zero short prompting: Directly giving the instruction to the model
system_prompt = "You should only answer the coding related question! your name is 'opta202'. if any one ask anything other than coding  then just say sorry!"

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": "what is the dictionary in python"
        }
    ]
)

print(response.choices[0].message.content)