from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
 
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()


template = PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

print(template.format(topic='Black Holes'))

chain = template | model | parser

result = chain.invoke({'topic': 'Black Holes'})

print(result)  # Output: {'facts': ['Black holes are regions in space where the gravitational pull is so strong that nothing, not even light, can escape from them.', 'They are formed when massive stars collapse under their own gravity at the end of their life cycle.', 'Black holes can be detected by observing the effects of their gravity on nearby objects and light.', 'There are different types of black holes, including stellar black holes, supermassive black holes, and intermediate black holes.', 'The study of black holes is crucial for understanding the fundamental laws of physics and the nature of the universe.']}
# Output: {'facts': ['Black holes are regions in space where the gravitational pull is so strong that nothing, not even light, can escape from them.', 'They are formed when massive stars collapse under their own gravity at the end of their life cycle.', 'Black holes can be detected by observing the effects of their gravity on nearby objects and light.', 'There are different types of black holes, including stellar black holes, supermassive black holes, and intermediate black holes.', 'The study of black holes is crucial for understanding the fundamental laws of physics and the nature of the universe.']}

