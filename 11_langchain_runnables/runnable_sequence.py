from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)
prompt2 = PromptTemplate(
    template="explain the following joke {text}",
    input_variables=["topic"]
)

model = ChatOpenAI(model="gpt-4.1")

parser = StrOutputParser()

chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)
response = chain.invoke({'topic': 'whiskey'})

print(response)