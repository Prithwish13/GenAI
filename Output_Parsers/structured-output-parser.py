from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_core.prompts import PromptTemplate

 
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give 3 fact about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)


chain = template | model | parser
result = chain.invoke({'topic': 'Black Holes'})
print(result)  # Output: {'fact_1': 'Black holes are regions in space where the gravitational pull is so strong that nothing, not even light, can escape from them.', 'fact_2': 'They are formed when massive stars collapse under their own gravity at the end of their life cycle.', 'fact_3': 'Black holes can be detected by observing the effects of their gravity on nearby objects and light.'}