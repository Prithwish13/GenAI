from dotenv import load_dotenv
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from typing import Optional, Literal
from pydantic import BaseModel
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate




load_dotenv()



class FeedbackResult(BaseModel):
    is_good: bool
    reason: Optional[str]


class State(TypedDict):
    user_query: str
    llm_output: Optional[str]
    is_good: Optional[bool]
    
    
llm = ChatOpenAI(model="gpt-5")
feedback_llm = ChatOpenAI(model="gpt-4o-mini")
feedback_prompt = ChatPromptTemplate.from_template(
    "You are a feedback evaluator.\n"
    "User query: {query}\n"
    "LLM response: {output}\n\n"
    "Decide if the response correctly and directly answers the user query.\n"
    "Respond in JSON only.\n\n"
    "{format_instructions}"
)
parser = PydanticOutputParser(pydantic_object=FeedbackResult)
    
def chat_bot(state: State):
    print("chat bot", state)
    response = llm.invoke(state.get("user_query"))
    state["llm_output"] = response.content
    return state

def chatbot_gemini(state: State):
    print("chatbot gemini", state)
    llm2 = ChatOpenAI(model="gpt-4.1-mini")
    response = llm2.invoke(state.get("user_query"))
    state["llm_output"] = response.content
    return state


def feedback_node(state: State) -> Literal["chatbot_gemini", "end_node"]:
    print("feedback node", state)
    user_query = state.get("user_query", "")
    llm_output = state.get("llm_output", "")
    
    prompt = feedback_prompt.format_prompt(query=user_query, output=llm_output, format_instructions=parser.get_format_instructions())
    
    response = feedback_llm.invoke(prompt.to_messages())
    feedback = parser.parse(response.content)
    print("Feedback:", feedback)
    state["is_good"] = feedback.is_good
    
    if feedback.is_good:
        return "end_node"
    
    return "chatbot_gemini"

def end_node(state: State):
    print("end node", state)
    return state
    
    
graph_builder = StateGraph(State)

graph_builder.add_node("chat_bot", chat_bot)
graph_builder.add_node("chatbot_gemini", chatbot_gemini)
graph_builder.add_node("end_node", end_node)

graph_builder.add_edge(START, "chat_bot")
graph_builder.add_conditional_edges("chat_bot", feedback_node)
graph_builder.add_edge("chatbot_gemini", "end_node")
graph_builder.add_edge("end_node", END)

graph = graph_builder.compile()

updated_state = graph.invoke(State({"user_query": "Hey there! What is my name?"})) 

print("Updated State", updated_state)