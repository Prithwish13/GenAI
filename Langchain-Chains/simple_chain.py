from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

prompt = PromptTemplate(
    template="Generate 5 interesting fact about {topic}.",
    input_variables=["topic"],
)

llm = ChatOpenAI(model="gpt-4")

parser = StrOutputParser()

chain = prompt | llm | parser

result = chain.invoke({"topic": "Python programming language"})

print(result)  # Output: A string containing an interesting fact about Python programming language.


# chain graph

chain.get_graph().print_ascii()