from mem0 import Memory
from dotenv import load_dotenv
from openai import OpenAI
import json
import os


load_dotenv()

OPEN_AI_API_KEY = os.getenv("OPENAI_API_KEY")



client = OpenAI()

# config
config = {
    "version": "v1.1",
    "embedder": {
        "provider": "openai",
        "config": {"api_key": OPEN_AI_API_KEY, "model": "text-embedding-3-small"}
    },
    "llm": {
        "provider": "openai",
        "config": {"api_key": OPEN_AI_API_KEY, "model": "gpt-4.1"}
    },
    "graph_store": {
        "provider": "neo4j",
        "config": {
            "url": os.getenv("NEO_URI"),
            "username": os.getenv("NEO_USER"),
            "password": os.getenv("NEO_PASSWORD")
        }
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6333
        }
    }    
}

mem_client = Memory.from_config(config)

while True:

    user_query = input("👤 \n")
    
    if user_query.lower() == "exit":
        break
    
    search_memory = mem_client.search(query=user_query, user_id="prithwishdey")
    
    memories = [f"ID: {mem.get("id")}, \n memory: {mem.get("memory")}" for mem in search_memory.get("results") ]
    
    print(f"Found memories {memories}")
    
    SYSTEM_PROMPT = f"""
        Here is the context about the user:
        {json.dumps(memories)}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_query}
        ]
    )

    ai_response = response.choices[0].message.content

    print(f"🤖 {ai_response}")

    mem_client.add(
        user_id="prithwishdey",
        messages=[
            {"role": "user", "content": user_query},
            {"role": "agent", "content": ai_response},
            
        ]
    )

print("The memory has been saved")