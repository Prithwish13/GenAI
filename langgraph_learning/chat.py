from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI


load_dotenv()

llm = ChatOpenAI(model="gpt-5")

class State(TypedDict):
    messages: Annotated[list, add_messages]
    
graph_builder = StateGraph(State)    

# node

def chatbot(state: State):
    response = llm.invoke(state.get("messages"))
    return {"messages": [response]}

def sample_node(state: State):
    response = llm.invoke(state.get("messages"))
    return {"messages": [response]}
    
    
    
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("sample_node", sample_node)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", "sample_node")
graph_builder.add_edge("sample_node", END)

graph = graph_builder.compile()

update_state = graph.invoke(State({"messages": "Hi, my name is Prithwish Dey"}))

print("Updated State", update_state)