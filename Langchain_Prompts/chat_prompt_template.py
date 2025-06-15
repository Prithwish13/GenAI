from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

chat_template = ChatPromptTemplate(
   [ 
    ('system', 'you are a helpful {domain} expert'),
    ('human', 'what is {topic}?')
    # SystemMessage(
    #     content="you are a helpful {domain} expert"
    # ),
    # HumanMessage(
    #     content="what is {topic}?"
    # )
    ]
)


prompt = chat_template.invoke({
    'domain': 'Angular',
    'topic': 'ngrx'
})

print(prompt)  # Output: you are a helpful Angular expert