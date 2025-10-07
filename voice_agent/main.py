import asyncio
import speech_recognition as sr
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# from pathlib import Path
from openai import AsyncOpenAI
from openai.helpers import LocalAudioPlayer


load_dotenv()

model = ChatOpenAI(model="gpt-4.1")




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



def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        
        r.pause_threshold = 2
        SYSTEM_PROMPT = """
            You are a expert voice agent. You will receive the transcript of what user has said using voice.
            You need to output as if you are an expert voice agent.
            
            What ever you response, It will converted to speech using TTS and played back to user.
            """
        messages = [
             SystemMessage(content=SYSTEM_PROMPT)
        ]
        while True:
            print("Please say something:")
            audio = r.listen(source)
            print("Recognizing...")
            try:
                text = r.recognize_google(audio)
                if text.lower() in ["exit", "quit", "stop"]:
                    print("Exiting...")
                    break
                 # Append user message to the conversation
                messages.append(HumanMessage(content=text))  
                model_response = model.invoke(messages)
                print(f"You said: {text}")
                print(f"AI Response: {model_response.content}")
                messages.append(AIMessage(content=model_response.content))
                 # Convert the model response to speech and play it
                asyncio.run(tts(model_response.content) )
            
                print("Response converted to speech and saved as 'speech.mp3'")  
            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
            
            
if __name__ == "__main__":
    main()