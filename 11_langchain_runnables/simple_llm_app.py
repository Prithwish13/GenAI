from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model_name="gpt-4.1", temperature=0.7)

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Suggest a catchy blog title about {topic} "
)


topic = input("Enter a topic")

formatted_prompt = prompt.format(topic=topic)

blog_title = llm.invoke(formatted_prompt)

print("Generated blog title is ", blog_title)