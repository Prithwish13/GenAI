from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
 
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

# 1st prompt
template1 = PromptTemplate(
    template="Write a detailed report on the topic: {topic}",
    input_variables=["topic"]
)


# 1st prompt
template2 = PromptTemplate(
    template="Write a 5 line summary on the following text. /n {text}",
    input_variables=["text"]
)

prompt1 = template1.invoke({'topic': 'Black Holes'})
res1 = model.invoke(prompt1)

prompt2 = template2.invoke({'text': res1.content})

res2 = model.invoke(prompt2)
print(res2.content)  # Output: A black hole is a region in space where the gravitational pull is so strong that nothing, not even light, can escape from it. They are formed when massive stars collapse under their own gravity at the end of their life cycle. Black holes can be detected by observing the effects of their gravity on nearby objects and light. There are different types of black holes, including stellar black holes, supermassive black holes, and intermediate black holes. The study of black holes is crucial for understanding the fundamental laws of physics and the nature of the universe.