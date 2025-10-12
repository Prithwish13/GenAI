from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnablePassthrough, RunnableBranch
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)
prompt2 = PromptTemplate(
    template="Summarize the following \n {text}",
    input_variables=["text"]
)


model = ChatOpenAI()

parser = StrOutputParser()

# report_gen_chain = RunnableSequence(prompt1, model, parser)

# alternative way declare the sequential chain
report_gen_chain = prompt1 | model | parser

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 500, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)

response = final_chain.invoke({'topic': 'fullstack developers'})


print(response)