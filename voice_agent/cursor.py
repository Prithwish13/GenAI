import os
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel, Field
from typing import Optional
import json
import requests

import asyncio
import speech_recognition as sr
from openai import AsyncOpenAI
from openai.helpers import LocalAudioPlayer

load_dotenv()

class WeatherOutput(BaseModel):
    step: str = Field(..., description="The ID of the steps. Example: PLAN, OUTPUT, TOOL, etc")
    content: Optional[str] = Field(None,  description="The Optional string contains the step")
    tool: Optional[str] = Field(None, description="The Id of the tool to call")
    input: Optional[str] = Field(None, description="The Input Provided by the user and input params to the tool")


client = OpenAI()
async_client = AsyncOpenAI()

async def tts(text):
    client = AsyncOpenAI()
    # speech_file_path = Path(__file__).parent / "speech.mp3"
    async with client.audio.speech.with_streaming_response.create(
    model="gpt-4o-mini-tts",
    voice="ash",
    input=text,
    instructions="Speak in a Sincere, empathetic, with genuine concern for the customer and understanding of the situation.",
    response_format="pcm",
    ) as response:
        # Stream the audio response to a file
        # response.stream_to_file(speech_file_path)
        
        # Play the audio response directly
        await LocalAudioPlayer().play(response)




system_prompt = """
    You're an expert AI Assistant in resolving user queries using chain of thought.
    You work on START, PLAN and OUTPUT steps.
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.
    You can also call a tool if required from the list of available tools.
    for every tool call wait for the observe step which is the output from the called tool
    If you are unable to fetch or process the retry

    Rules:
    - Strictly Follow the given JSON output format
    - Only run one step at a time.
    - The sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to the displayed to the user).

    Output JSON Format:
    { "step": "START" | "PLAN" | "OUTPUT" | "TOOL", "content": "string", "tool": "string", "input": "string" }
    
    Available Tools:
    - get_weather(city: str): Takes city name and returns weather info about the city.
    - run_command(command: str): Takes system linux command, execute the command to the user system and return the response

    Example 1:
    START: Hey, Can you solve 2 + 3 * 5 / 10
    PLAN: { "step": "PLAN": "content": "Seems like user is interested in math problem" }
    PLAN: { "step": "PLAN": "content": "looking at the problem, we should solve this using BODMAS method" }
    PLAN: { "step": "PLAN": "content": "Yes, The BODMAS is correct thing to be done here" }
    PLAN: { "step": "PLAN": "content": "first we must multiply 3 * 5 which is 15" }
    PLAN: { "step": "PLAN": "content": "Now the new equation is 2 + 15 / 10" }
    PLAN: { "step": "PLAN": "content": "We must perform divide that is 15 / 10  = 1.5" }
    PLAN: { "step": "PLAN": "content": "Now the new equation is 2 + 1.5" }
    PLAN: { "step": "PLAN": "content": "Now finally lets perform the add 3.5" }
    PLAN: { "step": "PLAN": "content": "Great, we have solved and finally left with 3.5 as ans" }
    OUTPUT: { "step": "OUTPUT": "content": "3.5" }
    
    Example 2:
    START: What is the weather like Kolkata?
    PLAN: { "step": "PLAN": "content": "Seems like user is interested in getting weather data of Kolkata" }
    PLAN: { "step": "PLAN": "content": "Lets see if we have available tool form the list of available tool" }
    PLAN: { "step": "PLAN": "content": "Great, We have get_weather tool for this query" }
    PLAN: { "step": "PLAN": "content": "I need to call get_weather with the city" }
    PLAN: { "step": "TOOL": "tool": "get_weather" "input": "kolkata" }
    PLAN: { "step": "OBSERVE": "tool": "get_weather", "output": "The temp of kolkata is cloudy with 20 C" }
    PLAN: { "step": "PLAN": "content": "Great, I got the weather info about kolkata" }
    OUTPUT: { "step": "OUTPUT": "content": "The cuurent weather in kolkata is 20 C with some cloudy sky." }
   
    
"""

def get_weather(city: str):
    weather_url=f"https://wttr.in/{city.lower}?format=%c+%t"
    response = requests.get(weather_url)
    
    print(response.text, response.status_code)
    
    return f"The weather in {city} is {response.text}"

def run_command(command: str):
    return os.system(command)


available_tool = {
    "get_weather": get_weather,
    "run_command": run_command
}

message_history = [
    {"role": "system", "content": system_prompt}
]
r = sr.Recognizer()
r.pause_threshold = 2
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    while True:
        print("Please say something:")
        audio = r.listen(source)
        print("Recognizing...") 
        try:
            user_query = r.recognize_google(audio)
            if user_query.lower() == "exit":
                break
            message_history.append({"role": "user", "content": user_query})
            while True:
                response = client.chat.completions.parse(
                    model="gpt-4.1",
                    response_format=WeatherOutput,
                    messages=message_history
                )
                raw_result = response.choices[0].message.content
                message_history.append({"role": "assistant", "content": raw_result})
                parsed_result = response.choices[0].message.parsed
                
                if parsed_result.step == "START":
                    print("🔥", parsed_result.content)
                    continue
                if parsed_result.step == "PLAN":
                    print("🧠", parsed_result.content)
                    continue
                if parsed_result.step == "TOOL":
                    tool_to_call = parsed_result.tool
                    tool_input = parsed_result.input
                    print(f"🧰: {tool_to_call} {tool_input}")
                    
                    tool_response = available_tool.get(tool_to_call)(tool_input)
                    
                    print(f"🧰: response {tool_to_call} {tool_input} response is {tool_response}")
                    message_history.append({
                        "role": "developer", "content": json.dumps(
                            {"step": "OBSERVE", "tool": tool_to_call, "input": tool_input, "output": tool_response}
                        )
                    })
                    
                if parsed_result.step == "OUTPUT":
                    asyncio.run(tts(parsed_result.content))
                    break
        except sr.UnknownValueError as e:
            print("Error:", str(e))
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
    

print("\n\n\n type exit to exit from the agent")