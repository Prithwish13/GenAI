from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.mongodb import MongoDBSaver
import os


load_dotenv()

DB_URI = os.getenv("MONGODB_URI")

llm = ChatOpenAI(model="gpt-5")

class State(TypedDict):
    messages: Annotated[list, add_messages]
    
graph_builder = StateGraph(State)    

# node

def chatbot(state: State):
    response = llm.invoke(state.get("messages"))
    return {"messages": [response]}


    
    
    
graph_builder.add_node("chatbot", chatbot)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()

def compile_graph_with_checkpointer(checkpointer):
    return graph_builder.compile(checkpointer=checkpointer)

# Before running this you need to add certificate in your venv terminal <export SSL_CERT_FILE=$(python -c "import certifi; print(certifi.where())")>

with MongoDBSaver.from_conn_string(DB_URI) as checkpointer:

    graph_with_memory = compile_graph_with_checkpointer(checkpointer)

    config = {
            "configurable": {
                "thread_id": "prithwish_thread_1",
            }
        }

    for chunk in graph_with_memory.stream(State({"messages": "what is my name?"}), config=config, stream_mode="values"):

        chunk["messages"][-1].pretty_print()
