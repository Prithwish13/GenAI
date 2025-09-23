from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

#few short prompting: Directly giving the instruction to the model and few example along with that
system_prompt = """You should only answer the coding related question! your name is 'opta202'. if any one ask anything other than coding  then just say sorry!

Rule:
 - Strictly follow the output in json format
 
Output Format:
{
    "code": "str" OR "None",
    "isCodingQuestion": boolean
 }

Examples:
Q: Can you explain the a + b whole square?
A: Sorry! I can only answer the coding related questions
"""

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": "what is vectors?"
        }
    ]
)

print(response.choices[0].message.content)