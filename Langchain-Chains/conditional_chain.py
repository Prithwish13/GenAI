from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatOpenAI(model="gpt-4")

parser = StrOutputParser()


class FeedBackSentiment(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="The sentiment of the feedback text")
    
# Define the output parser for the sentiment classification
sentiment_parser = PydanticOutputParser(pydantic_object=FeedBackSentiment)

prompt1 = PromptTemplate(
    template="Classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instructions}",
    input_variables=["feedback"],
    partial_variables={"format_instructions": sentiment_parser.get_format_instructions()},  
)

classifier_chain = prompt1 | model | sentiment_parser

prompt2 = PromptTemplate(
    template="Write an appropriate response to this positive feedback \n {feedback}",
    input_variables=["feedback"],
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

# Define a branch for sentiment classification
# branch = RunnableBranch(
#     (lambda x: getattr(x, "sentiment", "").strip().lower() == "positive", prompt2 | model | parser),
#     (lambda x: getattr(x, "sentiment", "").strip().lower()  == "negative", prompt3 | model | parser),
#     RunnableLambda(lambda x: "could not find sentiment")
# )

branch = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x:x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment")
)

chain = classifier_chain | branch

result = chain.invoke({"feedback": "I love the new features of this product!"})

print(result)  # Output: A string containing the appropriate response to the positive feedback