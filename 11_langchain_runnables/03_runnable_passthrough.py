from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnablePassthrough
from dotenv import load_dotenv


load_dotenv()

passthrough = RunnablePassthrough()


prompt1 = PromptTemplate(
    template="generate a joke about {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Explain the following joke {topic}",
    input_variables=["topic"]
)

model = ChatOpenAI()

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt1, model, parser)

exp_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(joke_gen_chain, exp_chain)

response = final_chain.invoke({'topic': 'fish finger'})

print(response.get('joke'))
print('\n\n\n')
print(response.get('explanation'))