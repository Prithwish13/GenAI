from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Create a chat prompt template with a placeholder for messages

chat_template = ChatPromptTemplate(
    messages=[
        ('system', 'You are a helpful customer support agent.'),
        MessagesPlaceholder(variable_name='chat_history'),
        ('human', '{query}'),
    ]
)

# load chat history
chat_history = []

with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())
    
print(chat_history)

prompt = chat_template.invoke({
    'chat_history': chat_history,
    'query': 'Where is my refund?'
})
print(prompt)  # Output: You are a helpful customer support agent. <chat history> Where is my refund?