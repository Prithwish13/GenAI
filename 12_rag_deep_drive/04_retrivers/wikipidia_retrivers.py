from langchain_community.retrievers import WikipediaRetriever
from dotenv import load_dotenv

load_dotenv()

retriever = WikipediaRetriever(top_k_results=2, lang="en")

query = "What is LangChain?"

result = retriever.invoke(query)

for i, doc in enumerate(result):
    print(f"\n----Result {i+1} ------ ")
    print(f"content:\n{doc.page_content}...")

