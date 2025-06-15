from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
  repo_id="deepseek-ai/DeepSeek-R1",
  provider="together"
)
model = ChatHuggingFace(llm=llm, max_tokens=10)
result = model.invoke("What is the capital of India")

print(result.content)