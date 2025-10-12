from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()


llm = ChatOpenAI(model_name="gpt-4.1")
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Suggest a catchy blog title about {topic} "
)

chain = prompt | llm
topic = input("Enter a topic: ")
blog_title = chain.invoke(topic)

print("Generated blog title is ", blog_title.content)
